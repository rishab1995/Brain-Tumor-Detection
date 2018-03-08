import cv2
import numpy as np
from skimage import measure

class Segment:
    def __init__(self,segments=5):
        #define number of segments, with default 5
        self.segments=segments

    def noise_removal(self, image):
        image_noiseless = cv2.medianBlur(image, 3)
        image_noiseless=cv2.GaussianBlur(image,(7,7),0)
        return image_noiseless

    def kmeans(self,image):
        image=cv2.GaussianBlur(image,(7,7),0)
        vectorized=image.reshape(-1,3)
        vectorized=np.float32(vectorized) 
        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        ret,label,center=cv2.kmeans(vectorized,self.segments,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
        res = center[label.flatten()]
        segmented_image = res.reshape((image.shape))
        return label.reshape((image.shape[0],image.shape[1])),segmented_image.astype(np.uint8)


    def extractComponent(self,image,label_image,label):
        component=np.zeros(image.shape,np.uint8)
        component[label_image==label]=image[label_image==label]
        return component

    def image_gray_scale(self, image):
        image_gray = cv2.cvtColor( image, cv2.COLOR_RGB2GRAY)
        return image_gray


if __name__=="__main__":
    import argparse
    import sys
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    ap.add_argument("-n", "--segments", required = False, type = int,
        help = "# of clusters")
    args = vars(ap.parse_args())
    image=cv2.imread(args["image"])
    cv2.imshow("Original",image) #original image

    if len(sys.argv)==3: 
        seg = Segment()
        label,result= seg.kmeans(image)
    else:
        seg=Segment(args["segments"])
        label,result=seg.kmeans(image)
     
    cv2.imshow("segmented",result) #image after segmentation

    result=seg.extractComponent(image,label,0)
    result_img = seg.image_gray_scale(result)
    
    cv2.imshow("extracted",result_img)
    cv2.waitKey(0)
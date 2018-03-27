import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

img = cv2.imread('tum.jpg' , 0)
#img2 = np.array(list(img))
gray_image = np.array(list(img))
print(gray_image)


data_grey= gray_image.reshape(-1) #1d array
#print(data_grey)
back_gray_image = data_grey.reshape(-1,180)
print(len(back_gray_image))

dg = np.float32(data_grey).reshape(-1,1)
print(dg)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness,labels,centers = cv2.kmeans(dg,4,None,criteria,10,flags)
print(labels)
l = labels.reshape(-1) #1d array
print(l)


#cv2.imshow('img', gray_image)
#cv2.imshow('img2',back_gray_image)  

labels_zero = []
i=0
for k in l:
	if k == 0:
		labels_zero.append(data_grey[i])
	else:
		labels_zero.append(255)
	i = i+1
#print(labels_zero)
seg_image = np.array(labels_zero)
seg_image = seg_image.reshape(-1,180)
print(len(seg_image))
cv2.imshow('seg' , seg_image)
cv2.waitKey(0) 
#plt.show()
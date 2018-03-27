import numpy as np 
from PIL import Image
from sklearn.cluster import KMeans
def segmentation(image):
	im_grey = im.convert("L")
	#print(im_grey)
	im_grey.show();
	data_grey = list(im_grey.getdata())
	#print(len(data_grey))
	dg = np.array(data_grey)
	kmeans = KMeans(n_clusters=4, random_state=0).fit(dg.reshape(-1,1))
	labels = list(kmeans.labels_)
	return labels, data_grey

from matplotlib import pyplot as py
import numpy as np 
from PIL import Image
from sklearn.cluster import KMeans

im = Image.open("tum.jpg")
#im.show()
data = list(im.getdata())
im_grey = im.convert("L")
print(im_grey)
im_grey.show();
data_grey = list(im_grey.getdata())
print(len(data_grey))
dg = np.array(data_grey)
kmeans = KMeans(n_clusters=4, random_state=0).fit(dg.reshape(-1,1))
labels = list(kmeans.labels_)
d1 = []
d2 = []
d3 = []
d4 = []
k=0
for i in labels:
	if i==0:
		d1.append(data_grey[k])
		d2.append(255)
		d3.append(255)
		d4.append(255)
	elif i==1:
		d1.append(255)
		d2.append(data_grey[k])
		d3.append(255)
		d4.append(255)
	elif i==2:
		d1.append(255)
		d2.append(255)
		d3.append(data_grey[k])
		d4.append(255)
	elif i==3:
		d1.append(255)
		d2.append(255)
		d3.append(255)
		d4.append(data_grey[k])
	k=k+1
#image_new = Image.fromarray(np.array(d1).reshape(-1,640))
#image_new.show()
Image.fromarray(np.array(d1).reshape(-1,180)).show()
Image.fromarray(np.array(d2).reshape(-1,180)).show()
Image.fromarray(np.array(d3).reshape(-1,180)).show()
Image.fromarray(np.array(d4).reshape(-1,180)).show()
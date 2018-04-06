from matplotlib import pyplot as py
import numpy as np 
from PIL import Image
from sklearn.cluster import KMeans
import MySQLdb
import base64

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="images")
x = conn.cursor()
try:
	r=raw_input("Enter name of image:")
	
	with open("C:\\Users\\abc\\Anaconda2\\MajorProject\\"+r+".jpg","rb") as blob:
		pic_read=blob.read()
		#encoded_pic=base64.encodestring(pic_read)
		x.execute("INSERT INTO img VALUES (%s,%s)",(pic_read,pic_read))
		im = Image.open(r+".jpg")
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
	print "Image added into database successfully"
	conn.commit()
except Exception as e:
   print e
   #conn.rollback()
   print "sdfgh"
finally:
    conn.close()		
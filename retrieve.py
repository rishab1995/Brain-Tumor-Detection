import MySQLdb
import sys
from matplotlib import pyplot as py
import numpy as np 
from PIL import Image
from sklearn.cluster import KMeans
import base64
from PIL import ImageFile


conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="images")
x = conn.cursor()
try:
	with open('C:\\Users\\abc\\Anaconda2\\MajorProject\\tum2.jpg','wb') as blob:
		x.execute("select images from img where img_id=11")
		data = x.fetchone ()[0]
		blob.write(data)
		#blob.decode('base64')
		#with open(,"rb") as blob_read:	
	with open('C:\\Users\\abc\\Anaconda2\\MajorProject\\tum2.jpg',"rb") as blob:
		pic_read=blob.read()
		ImageFile.LOAD_TRUNCATED_IMAGES = True
		
		im = Image.open(blob)
		print(im)
		im.show()
		conn.commit()
except Exception as e:
   print e
   #conn.rollback()
   print "sdfgh"
finally:
    conn.close()

	
'''for row in data :
	print row[0]
conn.commit()
#except:
 #  conn.rollback()
  # sys.exit()

blob=data[0]
print "%s"%blob
#print "%s"%data'''
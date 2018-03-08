import mysql.connector
from mysql.connector import errorcode
import base64

conn = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
x = conn.cursor()
try:
	with open("tum.jpg","rb") as blob:
		pic_read=blob.read()
		encoded_pic=base64.encodestring(pic_read)
	#path="C:\\Users\\abc\\Anaconda2\\MajorProject\\001.jpg"
		x.execute("INSERT INTO img VALUES (%s,%s)",(7,encoded_pic))
		conn.commit()
except Exception as e:
   print(e)
   #conn.rollback()
   print ("sdfgh")
finally:
    conn.close()






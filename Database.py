import serial
import time
import MySQLdb as mdb

arduino= serial.Serial("/dev/ttyACM0")
arduino.baudrate=9600
data=arduino.readline()
time.sleep(1)
data = arduino.readline()
pieces = data.split("  ")
#pieces = data.split("Humidity: ")
#pieces = data.split("Temperature: ")
#pieces = data.split("Heat index: ")

h=pieces[1]
t=pieces[3]
f=pieces[4]
hic=pieces[6]
hif=pieces[7]

con= mdb.connect('localhost','root','Deligence123','databasedht22');

with con:

        cursor=con.cursor()
        cursor.execute("""INSERT INTO DHT22 VALUES('',%s,%s,%s,%s,%s)""",(h,t,f,hic,hif))
        con.commit()
        cursor.close()



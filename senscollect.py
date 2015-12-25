#!  /usr/bin/python

import datetime
import serial
import telnetlib as Tnet

Hostaddress = "192.168.0.116"

ser = serial.Serial('/dev/ttyACM0',38400)
filename = "data_{0}".format(datetime.datetime.now().strftime('%d%m%y_%H%M%S'))
f = open(filename, "w");
tn = Tnet.Telnet(Hostaddress)
tn.write("I\n")
print tn.read_lazy()
tn.write("B\n")
print tn.read_lazy()

while 1:
	data = ser.readline()
        print data
	print datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	f.write("{0},{1}\r\n".format(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),data))
f.close()
tn.write("Z\n")
tn.close()

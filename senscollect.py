#!  /usr/bin/python

import datetime
import serial

class SensorRead():
    data = " "
    filename = " "
    ser = 0

    def open(self,filename):
        ser = serial.Serial('/dev/ttyACM0',38400)
        filename = "{0}_{1}".format(filename,datetime.datetime.now().strftime('%d%m%y_%H%M%S'))

    def getData(self):
	data = self.ser.readline()

    def writeData(self):
        f = open(self.filename, "w");
        print data
	print datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	f.write("{0},{1}\r\n".format(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),data))
        f.close()

    def close():
	self.file.close()
        self.ser.close()


if __name__ == '__main__':
	tst = SensorRead()
	tst.open("test")
	tst.close()
	

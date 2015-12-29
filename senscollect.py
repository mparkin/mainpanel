#!  /usr/bin/python

import datetime
import serial

class SensorRead():
    data = "none "
    filename = " "
    ser = 0

    def open(self,filename):
        self.ser = serial.Serial('/dev/ttyACM0',38400)
        self.filename = "{0}_{1}".format(filename,datetime.datetime.now().strftime('%d%m%y_%H%M%S'))

    def getData(self):
	self.data = self.ser.readline()

    def writeData(self):
        f = open(self.filename, "a");
        print self.data
	print datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
	f.write("{0},{1}\r\n".format(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),self.data))
        f.close()

    
    def close(self):
	self.f.close()
        self.ser.close()


if __name__ == '__main__':
	tst = SensorRead()
	tst.open("test")
        while(1):
            tst.getData()
            tst.writeData()

	tst.close()
	

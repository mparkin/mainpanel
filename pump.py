#! /usr/bin/python

import serial
import telnetlib as Tnet
import time

Hostaddress = "192.168.0.110"

class pumpControl():

    Hostaddress = "192.168.0.110"
    tn=Tnet.Telnet() 
    print "pc init"  
    data = "" 
    debug = False
    if debug:
        tn.set_debuglevel(5)

    def ComInit(self,address):
        self.Hostaddress = address
	print self.Hostaddress
        self.tn.open(self.Hostaddress,23)

    def init(self):
	self.tn.write("I\n")
        self.write_data("R","225")
        self.write_data("F","2900")
        self.write_data("S","207")
        self.readit()

    def speed(self,speed):
	self.write_data("S",speed)

    def fast(self,speed):
	self.write_data("F",speed)

    def radian(self,count):
	self.write_data("R",count)

    def winding(self,count):
	self.write_data("W",count)

    def duration(self,count):
	self.write_data("D",count)

    def turn(self,turns):
	self.tn.write("L\n")

    def timed(self,turns):
	self.tn.write("T\n")

    def home(self,turns):
	self.tn.write("H\n")

    def direction(self,dir):
 	if dir == 'C':
	    self.tn.write("C\n")
        else:
            self.tn.write("A\n")
        self.readit()

    def normal(self):
	self.tn.write("N\n")
        self.readit()

    def pulse(self):
	self.tn.write("P\n")
        self.readit()

    def brake(self,dir):
 	if dir == 'B':
	    self.tn.write("B\n")
        else:
            self.tn.write("U\n")
        self.readit()

    def stop(self):
	self.tn.write("E\n")
        self.readit()

    def start(self,filename):
	if filename == "freerun":
            self.tn.write("G\n")
            self.readit()
        else:
            self.seqrun(filename);

    def quit(self):
	self.tn.write("Z\n")
        self.readit()

    def info(self):
	self.tn.write("X\n")
        self.readit()

    def readit(self):
        time.sleep(1)
	self.data = self.tn.read_very_eager()
	if self.debug:
            print(self.data)
    
    def write_data(self,command,data):
	strings = [command,data]
        #print '\n'.join(strings)
	self.tn.write('\n'.join(strings))
        self.readit()

    def seqrun(self,filename):
	f = open(filename,'r')
        for line in f:
            mod = False
            cmd = line.split()
	    for idx,val in enumerate(cmd):
                print idx,val
                if idx == 0:
                    command = val
                if idx == 1:
                    mod = True
                    modifier = val
                    print modifier
            if command == "Run":
                self.tn.write("G\n")
                self.readit()
                if mod:
                   time.sleep(float(modifier)/1000)
            if command == "Wait":
                if mod:
                   time.sleep(float(modifier)/1000)
            if command == "Flow":
	        self.speed(modifier)
            if command == "Stop":
                self.stop()
            if command == "Withdraw":
                self.direction('A')
            if command == "Dispense":
                self.direction('C')
            if command == "Pulse":
                self.pulse()
                if mod:
                   time.sleep(float(modifier)/1000)
                mod = False
            if command == "Normal":
                self.normal()
                if mod:
                   time.sleep(float(modifier)/1000)
                mod = False
        f.close()

def runit():
    p = pumpControl()
    p.debug = True
    p.ComInit("192.168.0.110")
    p.info()
    p.quit()


if __name__ == '__main__':
    runit()

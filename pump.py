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

    def ComInit(self,address):
        self.Hostaddress = address
	print self.Hostaddress
        self.tn.open(self.Hostaddress,23)

    def init(self):
	self.tn.write("I\n")
        self.readit()

    def speed(self,speed):
	strings = ["S",speed]
        print '\n'.join(strings)
	self.tn.write('\n'.join(strings))
        self.readit()

    def interval(self,interval):
	strings = ["D",interval]
        print '\n'.join(strings)
	self.tn.write('\n'.join(strings))
        self.readit()

    def turna(self,turns):
	strings = ["L",turns]
        print '\n'.join(strings)
	self.tn.write('\n'.join(strings))
        self.readit()


    def direction(self,dir):
 	if dir == 'C':
	    self.tn.write("C\n")
        else:
            self.tn.write("A\n")
        self.readit()

    def brake(self,dir):
 	if dir == 'B':
	    self.tn.write("B\n")
        else:
            self.tn.write("U\n")
        self.readit()

    def stop(self):
	self.tn.write("S\n")
        self.readit()

    def start(self):
	self.tn.write("B\n")
        self.readit()

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

def runit():
    p = pumpControl()
    p.debug = True
    p.ComInit("192.168.0.110")
    p.info()
    p.quit()


if __name__ == '__main__':
    runit()

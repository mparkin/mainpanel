#! /usr/bin/python

import serial
import telnetlib as Tnet

Hostaddress = "192.168.0.116"

class pumpControl():

    Hostaddress = "192.168.0.116"
    tn=Tnet.Telnet(); 
    print "pc init"   
    def ComInit(self,address):
        self.Hostaddress = address
	print self.Hostaddress
        self.tn.open(self.Hostaddress)

    def init(self):
	self.tn.write("I\n")
    def speed(self):
	self.tn.write("S2000\n")
    def direction(self):
	self.tn.write("C\n")
    def stop(self):
	self.tn.write("S\n")
    def start(self):
	self.tn.write("B\n")
    def quit(self):
	self.tn.write("Z\n")


def runit():
    p = pumpControl()
    p.ComInit("192.168.0.116")
    p.init()
    p.quit()


if __name__ == '__main__':
	runit()

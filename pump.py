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

    def speed(self,speed):
	strings = ["S",speed]
        print '\n'.join(strings)
	self.tn.write('\n'.join(strings))

    def interval(self,interval):
	strings = ["D",interval]
        print '\n'.join(strings)
	self.tn.write('\n'.join(strings))

    def turna(self,turns):
	strings = ["L",turns]
        print '\n'.join(strings)
	self.tn.write('\n'.join(strings))

    def direction(self,dir):
 	if dir == 'C':
	    self.tn.write("C\n")
        else:
            self.tn.write("A\n")

    def brake(self,dir):
 	if dir == 'B':
	    self.tn.write("B\n")
        else:
            self.tn.write("U\n")

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

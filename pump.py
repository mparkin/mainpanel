#! /usr/bin/python

import serial
import telnetlib as Tnet

Hostaddress = "192.168.0.116"

class pumpControl(object):

    tn = Tnet.Telnet(Hostaddress);

    def init():
	tn.write("I\n")
    def speed():
	tn.write("S2000\n")
    def direction():
	tn.write("C\n")
    def stop():
	tn.write("S\n")
    def start():
	tn.write("B\n")
    def quit():
	tn.write("Z\n")


def runit():
    p = pumpControl()
    p.init()


if __name__ == '__main__':
	runit()

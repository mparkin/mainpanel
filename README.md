# mainpanel.py

##Description

This is the operator interface to the pump control system. 
It talks to the pump(s) through a network connection and to two sensors;
Pressure sensor and a mass scale. These are connected to the operator
interface system via an arduino and a serial(USB) connection.

The message from the sensor arduino is in this format:
 <"last mass measurement","AVG mass", "Pressure">

The pump connection is through a socket connection to the controlleing
"Photon" board and a simple single character command set. 

## TO DO

1. Check for connection to pump. If not there send message and die
2. Add pump commands to this document.  



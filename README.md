# mainpanel.py

##Description

This is the operator interface to the pump control system. 
It talks to the pump(s) through a network connetion and to two sensors;
Pressure sensor and a mass scale. These are connected to the operator
interface system via an arduino and a serial(USB) connection.

The message from the arduino is in this format <"last mass measurement","AVG mass", "Pressure">

## TO DO

1. Check for connection to pump. If not there send message and die
 



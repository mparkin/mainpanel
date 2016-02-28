# mainpanel.py

##Description

This is the operator interface to the pump control system. 
It talks to the pump(s) through a network connection and to two sensors
dirctly connected via a serial port link.
The sensors are Pressure and mass scale. These are connected to the operator
interface system via an arduino and a serial(USB) connection.

The message from the sensor arduino is in this format:
 <"last mass measurement","AVG mass", "Pressure">

The pump connection is through a socket connection to the controlling
"Photon" board and a simple single character command set. 

Command Set

* A - anticlockwise 
* B - brake moter
* C - clockwise
* D - duration
* E - stop
* F - Hi speed Setting
* G - Go
* H - go to and stop a home position
* I - Init
* L - counted rotation run
* N - Normal run ( unpulse )
* P - Run at hardware set fast rate
* R - Fast run area by motor pulses
* S - Set speed ( 0-4095 , S1234 )
* T - Timed Run
* U - Unbrake motor
* W - number of rotations
* X - return status
* Z - End communications session


## TO DO

1. ~~Check for connection to pump. If not there send message and die~~
2. ~~Add pump commands to this document.~~  
3. Add action scheduler
4. Add configuration window
5. Add action button frame
6. Break out pump commands to own class ( pump.py )
7. Break out sensor commands to own class (sensors.py)

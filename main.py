#! /usr/bin/python

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.properties import BoundedNumericProperty
from kivy.properties import StringProperty

from settingsjson import settings_json

import datetime
import serial
import pump  
import senscollect
import time

ppump = pump.pumpControl()	


Builder.load_string('''
<Interface>:
    orientation: 'horizontal'
    size: root.size
    BoxLayout: 
        orientation: 'vertical'
        Label: 
            text: 'Pump Controls v0.7B'
        Button:
            text: 'Initialize'
            id: Initbutton
            on_release: root.initButton(self)
        Button: 
            text: str(root.flowrate)
            id: flowratebutton
            on_release: root.flowButton(self)
        Button:
            text: 'Dispense'
            id: directionbutton
            on_release: root.directionButton(self)
        Button:
            text: 'Stopped' 
            id: operationbutton
            on_release: root.runButton(self)
        Button:
            text: 'Interval' 
            id: intvbutton
            on_release: root.intervalButton(self)
        Button:
            text: 'Brake Off'
            id: brakebutton 
            on_release: root.brakeButton(self)
        Button:
            text: 'Normal' 
            id: methodbutton
            on_release: root.pulseButton(self)
        Button:
            text: 'Free Run'
            id: modebutton 
            on_release: root.modeButton(self)
        Button:
            text: 'Sequence Editor'
            id: editorbutton 
            on_release: root.editButton(self)
        Button:
            text: 'Sensor Recording'
            id: SensorButton 
            on_release: root.sensorButton(self)
        Button:
            text: 'Settings'
            id: settingsbutton
            on_release: app.open_settings()
    Label:
        text: 'Space Holder!!!!!'
    Label:
        text: 'Space Holder1!!!!'
    Label:
        text: 'Space Holder2!!!!'
    Label:
        text: 'Space Holder3!!!!'
    Label:
        text: 'Space Holder4!!!!'
''')

class Interface(BoxLayout):
    flowrate = BoundedNumericProperty( 0,min = 0, max = 171 )
    calnumber = BoundedNumericProperty( 24.06,min = 0, max = 100 )
    interval = NumericProperty( 100 )
    turns = NumericProperty( 24 )
    direction = "Dispense"
    mode = StringProperty("")
    flobutid = 0
    settings_cls = SettingsWithSidebar
    use_kivy_settings = False
    
    def initButton(self,id):
        id.background_color = [ 0, 1, 1, 1]
	ppump.init()
	self.ids.operationbutton.text = "Stopped"
        ppump.brake('B')
        self.ids.operationbutton.background_color = [ 1, 0, 0, 1]

    def directionButton(self,id):
        if id.text == "Dispense":
            ppump.direction('A')
            id.text = "Withdraw"
            id.background_color = [ 1, 1, 0, 1]
        else :
	    id.text = "Dispense"
	    ppump.direction('C')
            id.background_color = [ 0, 1, 1, 1]

    def brakeButton(self,id):
        if id.text == "Brake Off":
            ppump.brake('B')
            id.text = "Brake On"
            id.background_color = [ 1, 1, 0, 1]
        else :
	    id.text = "Brake Off"
	    ppump.brake('U')
            id.background_color = [ 0, 1, 1, 1]

    def flowButton(self,id):
        id.text = str(self.flowrate) 
        id.background_color = [ 1, 1, 1, 1]
        self.flobutid = id    
	ppump.speed(str(int(self.flowrate * 24.06)))

    def runButton(self,id):
        if id.text == "Stopped":
            id.text = "Running"
            id.background_color = [ 0, 1, 0, 1]
            if self.ids.modebutton.text == "Seq Run":
                ppump.start("./sequence.txt")
            else :
                ppump.start("freerun")
        else :
	    id.text = "Stopped"
            ppump.brake('B')
            id.background_color = [ 1, 0, 0, 1]

    def modeButton(self,id):
        if id.text == "Free Run":
            id.text = "Seq Run"
            id.background_color = [ 0, 0, 1, 1]
        else :
	    id.text = "Free Run"
            id.background_color = [ 0, 1, 0, 1]

    def editButton(self,id):
        id.background_color = [ 0, 1, 0, 1]
	ppump.start()

    def sensorButton(self,id):
        id.background_color = [ 0, 1, 0, 1]
	ppump.start()

    def intervalButton(self,id):
        id.background_color = [ 1, 0, 0, 1]
	ppump.duration(str(self.interval))

    def pulseButton(self,id):
        id.background_color = [ 1, 0, 0, 1]
	ppump.stop()

    def on_flowrate(self, instance, value):
	ppump.speed(str(int(value * self.calnumber)))

    def on_calnumber(self, instance, value):
	ppump.speed(str(int(value * self.flowrate)))

    def on_interval(self, instance, value):
	ppump.duration(str(value))

    def on_calnumber(self, instance, value):
	ppump.turn(str(value ))

    def seqrun(self, filename):
        f = open(filename,'r')
        for line in f:
            mode = False
            cmd = line.split()
            for idx , val in enumerate(cmd):
                print idx, val
                if idx == 0:
		    command = val
                if idx == 1:
                    modifier = val
                    mod = True
                    print modifier
            if command == "Run":
	        ppump.start()
                if mod:
                    time.sleep(float(modifier)/1000)
                mod = False
            if command == "Wait":
                if mod:
                    time.sleep(float(modifier)/1000)
                mod = False
            if command == "Stop":
                ppump.stop() 
            if command == "Withdraw":
	        ppump.direction('A')
            if command == "Dispense":
	        ppump.direction('C')
            if command == "Pulse":
	        ppump.start()
                if mod:
                    time.sleep(float(modifier)/1000)
                mod = False
            if command == "Flow":
                ppump.stop() 
        f.close()

class Mainpanelapp(App):

    intface = Interface()
    
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        ppump.ComInit(self.config.get('operation','PumpAddress'))
        ppump.init()
        self.intface.flowrate = float(self.config.get('operation','flowRate'))
        self.intface.calnumber = float(self.config.get('operation','calnumber'))
        self.intface.mode = self.config.get('operation','mode')
        return self.intface

    def build_config(self,config):
	config.setdefaults('operation', {
	    'boolexample': True,
	    'flowRate' : '15.0',
            'calnumber': '13.8',
            'interval': '24',
            'turns': '24',
	    'Mode' : 'Run',
            'PumpAddress'  : '192.168.0.110',
	    'dataDirectory'    : './' ,
	    'datafile'    : 'sensordata' })

    def build_settings(self,settings):
        settings.add_json_panel('Pump System Settings',
				self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        print config, section, key, value 
        if key == 'flowRate' :
		self.intface.flowrate = float(value)
        elif key == 'calnumber' :
		self.intface.calnumber = float(value)
        elif key == 'interval' :
		self.intface.interval = int(value)
        elif key == 'turns' :
		self.intface.turns = float(value)

if __name__ == '__main__':
	Mainpanelapp().run()
        ppump.quit()

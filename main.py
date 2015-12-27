#! /usr/bin/python

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.label import Label
from kivy.uix.button import Button

from settingsjson import settings_json

import datetime
import serial
import pump  

ppump = pump.pumpControl()	

Builder.load_string('''
<Interface>:
    orientation: 'horizontal'
    size: root.size
    BoxLayout: 
        orientation: 'vertical'
        Label: 
            text: 'Pump Controls'
        Button:
            text: 'Initialize'
            on_release: root.initButton(self)
        Button: 
            text: root.flowrate
            on_release: root.flowButton(self)
        Button:
            text: 'Dispense'
            on_release: root.directionButton(self)
        Button:
            text: 'Stopped' 
            on_release: root.runButton(self)
        Button:
            text: 'Interval' 
            on_release: root.stopButton(self)
        Button:
            text: 'Brake Off' 
            on_release: root.brakeButton(self)
        Button:
            text: 'Normal' 
            on_release: root.pulseButton(self)
        Button:
            text: 'FreeRun' 
            on_release: root.modeButton(self)
        Button:
            text: 'Sequence Editor' 
            on_release: root.editButton(self)
        Button:
            text: 'Sensor Recording' 
            on_release: root.editButton(self)
        Button:
            text: 'Settings'
            on_release: app.open_settings()
    Label:
        text: 'Space Holder!!!!'
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
    flowrate = "15 ml/min"
    def initButton(self,id):
        id.background_color = [ 0, 1, 1, 1]
	ppump.init()
    def directionButton(self,id):
        id.background_color = [ 1, 1, 0, 1]
	ppump.direction()
    def flowButton(self,id):
        id.text = "30 ml/min"
        id.background_color = [ 1, 1, 1, 1]
	ppump.speed()
    def runButton(self,id):
        id.background_color = [ 0, 1, 0, 1]
	ppump.start()
    def stopButton(self,id):
        id.background_color = [ 1, 0, 0, 1]
	ppump.stop()
    def pulseButton(self,id):
        id.background_color = [ 1, 0, 0, 1]
	ppump.stop()

class Mainpanelapp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        setting = self.config.get('operation', 'boolexample')
        ppump.ComInit("192.168.0.116")
        ppump.init()
        return Interface()

    def build_config(self,config):
	config.setdefaults('operation', {
	    'boolexample': True,
	    'numericexample' : 10,
	    'optionsexample' : 'option2',
            'stringexample'  : 'some_string',
	    'pathexample'    : '/some/path' })

    def build_settings(self,settings):
        settings.add_json_panel('Pump System Settings',
				self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        print config, section, key, value 
 
if __name__ == '__main__':
	Mainpanelapp().run()
        ppump.quit()

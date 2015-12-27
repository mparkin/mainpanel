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
#import telnetlib as Tnet
import pump  

ppump = pump.pumpControl()	

Builder.load_string('''
<Interface>:
    id: MainWindow
    orientation: 'horizontal'
    size: root.size
    BoxLayout: 
        orientation: 'vertical'
        Label: 
            text: 'Pump Controls'
        Button:
            text: 'Initialize'
            on_release: root.initButton()
        Button:
            text: 'Flow Rate'
            on_release: root.flowButton()
        Button:
            text: 'Direction'
            on_release: root.directionButton()
        Button:
            text: 'Run' 
            on_release: root.runButton()
        Button:
            text: 'Stop' 
            on_release: root.stopButton()
        Button:
            text: 'Mode' 
            on_release: root.modeButton()
        Button:
            text: 'Sequence Editor' 
            on_release: root.editButton()
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
    def initButton(self):
	ppump.init()
    def flowButton(self):
	ppump.flow()
    def runButton(self):
	ppump.run()
    def stopButton(self):
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

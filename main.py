#! /usr/bin/python

import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.label import Label

from settingsjson import settings_json

import datetime
import serial
import telnetlib as Tnet

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
#            on_release: app.open_settings()
        Button:
            text: 'Flow Rate'
#            on_release: app.open_settings()
        Button:
            text: 'Direction'
#            on_release: app.open_settings()
        Button:
            text: 'Run' 
#            on_release: app.open_settings()
        Button:
            text: 'Stop' 
#            on_release: app.open_settings()
        Button:
            text: 'Mode' 
#            on_release: app.open_settings()
        Button:
            text: 'Sequence Editor' 
#            on_release: app.open_settings()
        Button:
            text: 'Settings!'
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
    pass

class Mainpanelapp(App):	
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        setting = self.config.get('operation', 'boolexample')
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

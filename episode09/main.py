# -*- coding: utf-8 -*-
"""

Filename: main.py

Author:   Ednalyn C. De Dios
Phone:    (210) 236-2685
Email:    ednalyn.dedios@taskus.com 

Created:  March 4, 2020
Updated:  March 7, 2020

PURPOSE: describe the purpose of this script.

PREREQUISITES: list any prerequisites or
assumptions here.

DON'T FORGET TO:
1. Hydrate.
2. Sleep.
3. Have fun!

"""

# import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

from datetime import datetime

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock

now = datetime.now()
current_time = now.strftime("%m/%d/%Y %H:%M:%S")

class MyGrid(Widget):

    number1 = NumericProperty()
    number2 = NumericProperty()
    number3 = NumericProperty()

    title1 = ObjectProperty(None)
    title2 = ObjectProperty(None)
    title3 = ObjectProperty(None)

    time1 = ObjectProperty(None)
    time2 = ObjectProperty(None)
    time3 = ObjectProperty(None)

    button1 = ObjectProperty(None)
    button2 = ObjectProperty(None)
    button3 = ObjectProperty(None)

    message = ObjectProperty(None)

    button_reset = ObjectProperty(None)


    def __init__(self, **kwargs): 
  
        # The super() builtin 
        # returns a proxy object that 
        # allows you to refer parent class by 'super'.  
        super(MyGrid, self).__init__(**kwargs) 
  
        self.increment_time1(0)
  
    # To increase the time / count 
    def increment_time1(self, interval): 
        self.number1 += .1

    # To increase the time / count 
    def increment_time2(self, interval): 
        self.number2 += .1

    # To increase the time / count 
    def increment_time3(self, interval): 
        self.number3 += .1
  
    # To start the count 
    def start1(self):
        Clock.schedule_interval(self.increment_time1, .1) 

    # To start the count 
    def start2(self):
        Clock.schedule_interval(self.increment_time2, .1) 

     # To start the count 
    def start3(self):
        Clock.schedule_interval(self.increment_time3, .1) 
  
    # To stop the count / time 
    def stop1(self): 
        Clock.unschedule(self.increment_time1)
        if int(self.time1.text)/60 > 1:
            self.time1.text = str(int(int(self.time1.text)/60)) + 'm'
        else:
            self.time1.text = '<1m'

     # To stop the count / time 
    def stop2(self): 
        Clock.unschedule(self.increment_time2)
        if int(self.time2.text)/60 > 1:
            self.time2.text = str(int(int(self.time2.text)/60)) + 'm'
        else:
            self.time2.text = '<1m'

     # To stop the count / time 
    def stop3(self): 
        Clock.unschedule(self.increment_time3)
        if int(self.time3.text)/60 > 1:
            self.time3.text = str(int(int(self.time3.text)/60)) + 'm'
        else:
            self.time3.text = '<1m'


    def btn1(self):
        if self.button1.text == "Stop":
        	self.button1.text = "Start"
        	self.stop1()
        	self.message.text = self.title1.text + " stopped."
        else:
        	self.button1.text = "Stop"
        	self.start1()
        	self.message.text = self.title1.text + " started."

    def btn2(self):
        if self.button2.text == "Stop":
        	self.button2.text = "Start"
        	self.stop2()
        	self.message.text = self.title2.text + " stopped."
        else:
        	self.button2.text = "Stop"
        	self.start2()
        	self.message.text = self.title2.text + " started."

    def btn3(self):
        if self.button3.text == "Stop":
        	self.button3.text = "Start"
        	self.stop3()
        	self.message.text = self.title3.text + " stopped."
        else:
        	self.button3.text = "Stop"
        	self.start3()
        	self.message.text = self.title3.text + " started."

    def btn1_reset(self):
        self.save(str(current_time) + ',' + self.time1.text + ',' + self.title1.text + '\n')
        self.time1.text = "0"
        self.title1.text = ""
        self.button1.text = "Start"
        self.stop1()
        

    def btn2_reset(self):
        self.save(str(current_time) + ',' + self.time2.text + ',' + self.title2.text + '\n')
        self.time2.text = "0"
        self.title2.text = ""
        self.button2.text = "Start"
        self.stop2()
        

    def btn3_reset(self):
        self.save(str(current_time) + ',' + self.time3.text + ',' + self.title3.text + '\n')
        self.time3.text = "0"
        self.title3.text = ""
        self.button3.text = "Start"
        self.stop3()
        

    def btn_reset(self):
        App.get_running_app().stop()

    def save(self,entries):
        fob = open('multitasker.txt','a')
        write = fob.write(entries)

class MultitaskerApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
	MultitaskerApp().run()
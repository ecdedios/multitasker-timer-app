# -*- coding: utf-8 -*-
"""

Filename: main.py

Author:   Ednalyn C. De Dios
Phone:    (210) 236-2685
Email:    ednalyn.dedios@taskus.com 

Created:  March 4, 2020
Updated:  March 4, 2020

PURPOSE: describe the purpose of this script.

PREREQUISITES: list any prerequisites or
assumptions here.

DON'T FORGET TO:
1. Hydrate.
2. Sleep.
3. Have fun!

"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    title1 = ObjectProperty(None)
    title2 = ObjectProperty(None)
    title3 = ObjectProperty(None)

    def btn1(self):
        print("Title: ", self.title1.text)

    def btn2(self):
        print("Title: ", self.title2.text)

    def btn3(self):
        print("Title: ", self.title3.text)


class MultitaskerApp(App):
	def build(self):
		return MyGrid()


if __name__ == '__main__':
	MultitaskerApp().run()
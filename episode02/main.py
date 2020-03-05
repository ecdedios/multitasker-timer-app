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


class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 2

		self.add_widget(Label(text="Time Elapsed"))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)
		
		self.add_widget(Label(text="Time Elapsed"))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)
		
		self.add_widget(Label(text="Time Elapsed"))
		self.name = TextInput(multiline=False)
		self.add_widget(self.name)
		


class MultitaskerApp(App):
	def build(self):
		return MyGrid()


if __name__ == '__main__':
	MultitaskerApp().run()
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

class MultitaskerApp(App):
	def build(self):
		return Label(text="Hello, from Dd.")

if __name__ == '__main__':
	MultitaskerApp().run()
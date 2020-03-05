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


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1 # Set columns for main layout

        self.inside = GridLayout() # Create a new grid layout
        self.inside.cols = 3 # set columns for the new grid layout

        # ALL OF THESE ARE APART OF THE (INTERIOR)NEW LAYOUT
        self.inside.add_widget(Label(text="00:00", font_size=40))
        self.title1 = TextInput(multiline=True, font_size=32)
        self.inside.add_widget(self.title1)
        self.submit1 = Button(text="Start", font_size=40)
        self.submit1.bind(on_press=self.pressed1)  
        self.inside.add_widget(self.submit1)

        self.inside.add_widget(Label(text="00:00", font_size=40))
        self.title2 = TextInput(multiline=True, font_size=32)
        self.inside.add_widget(self.title2)
        self.submit2 = Button(text="Start", font_size=40)
        self.submit2.bind(on_press=self.pressed2)  
        self.inside.add_widget(self.submit2)

        self.inside.add_widget(Label(text="00:00", font_size=40))
        self.title3 = TextInput(multiline=True, font_size=32)
        self.inside.add_widget(self.title3)
        self.submit3 = Button(text="Start", font_size=40)
        self.submit3.bind(on_press=self.pressed3)  
        self.inside.add_widget(self.submit3)
        #-------------------------------------------------

        self.add_widget(self.inside) # Add the interior layout to the main
       
        self.add_widget(Label(text="Log messages goes here."))

    def pressed1(self, instance):
        title1 = self.title1.text
        print("Title #1: ", title1)

    def pressed2(self, instance):
        title2 = self.title2.text
        print("Title #2: ", title2)

    def pressed3(self, instance):
        title3 = self.title3.text
        print("Title #3: ", title3)
		


class MultitaskerApp(App):
	def build(self):
		return MyGrid()


if __name__ == '__main__':
	MultitaskerApp().run()
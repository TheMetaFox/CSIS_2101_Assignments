#File: TempCalcGUI.py
#Author: Joshua Peters
#Project: CSIS2101 Week13_Particip
#Version: 1.0 11.15.2020

#This program creates a GUI which converts temperature from Celsius to Fahrenheit
#   F = (C * 9/5) + 32

from tkinter import *
import tkinter.messagebox

class TempConverterGUI:
    def __init__(self):
        #Create main window
        self.main_window = tkinter.Tk()

        #Create tow frames top frame and bottom frame
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text = "Enter a temperature in Celsius: ")

        self.cels_entry = tkinter.Entry(self.top_frame,
                                         width = 10)

        self.prompt_label.pack(side = "left")
        self.cels_entry.pack(side = "left")

        self.descr_label = tkinter.Label(self.middle_frame,
                                         text = "Converted temperature in Fahrenheit.")

        #We create a stringVar Object with an output label to store the blank character
        self.value = tkinter.StringVar()

        self.fahr_label = tkinter.Label(self.middle_frame,
                                        textvariable = self.value)

        self.descr_label.pack(side = "left")
        self.fahr_label.pack(side = "left")

        self.conv_button = tkinter.Button(self.bottom_frame,
                                           text = "Convert",
                                           command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = "Quit",
                                          command = self.main_window.destroy)
        self.conv_button.pack(side = "top")
        self.quit_button.pack(side = "top")

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()



        #Enter the mainloop
        tkinter.mainloop()

    #This is the function that converts when button convert is clicked.
    def convert(self):
        #Get the value entered by the user in the fahr_entry
        cels = float(self.cels_entry.get())

        #Convert Fahrenheit into celsius

        fahr = (cels * 9/5) + 32

        self.value.set(fahr)

cels_conv = TempConverterGUI()

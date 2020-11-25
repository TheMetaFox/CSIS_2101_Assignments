#File:    PetersSpeedLimit.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.6 November 5, 2020

# This program calculates the speeding fine in different situations.

from tkinter import *

##HEIGHT = 250
##WIDTH = 350

class SpeedLimitGUI:
    def __init__(self):
        # Create root
        self.root = Tk()

        # Create canvas
##        self.canvas = Canvas(self.root,
##                             height= HEIGHT, width= WIDTH,
##                             bg= "#DADEE0")
##        self.canvas.pack()

        # Create top, middel, and bottom frames
        self.top_frame = Frame(self.root)
        self.top_frame.pack(side= TOP)
        self.middle_frame = Frame(self.root)
        self.middle_frame.pack(side= TOP)
        self.bottom_frame = Frame(self.root)
        self.bottom_frame.pack(side= BOTTOM)

        # Create limit, speed, & zone frames
        self.limit_frame = Frame(self.top_frame)
        self.limit_frame.pack()
        self.speed_frame = Frame(self.top_frame)
        self.speed_frame.pack()
        self.zone_frame = Frame(self.top_frame)
        self.zone_frame.pack()

        # Create fine & message frames
        self.fine_frame = Frame(self.middle_frame)
        self.fine_frame.pack()
        self.msg_frame = Frame(self.middle_frame)
        self.msg_frame.pack()

        # Create speed limit label & entry
        self.limit_label = Label(self.limit_frame,
                                 text= "The speed limit of the zone: ")
        self.limit_entry = Entry(self.limit_frame,
                                 bd= 2)

        self.limit_label.pack(side= LEFT)
        self.limit_entry.pack(side= RIGHT)
        
        # Create vihicle speed label & entry
        self.speed_label = Label(self.speed_frame,
                                 text= "The speed of the vehicle: ")
        self.speed_entry = Entry(self.speed_frame,
                                 bd= 2)

        self.speed_label.pack(side= LEFT)
        self.speed_entry.pack(side= RIGHT)

        # Create school/construction zone label, value, & button
        self.zone_var = IntVar()
        self.zone_label = Label(self.zone_frame,
                                text= "School or construction zone? ")
        self.zone_check = Checkbutton(self.zone_frame,
                                      offvalue= 0,
                                      onvalue= 1,
                                      variable= self.zone_var)

        self.zone_label.pack(side= LEFT)
        self.zone_check.pack(side= RIGHT)

        # Create fine amount display
        self.fine = StringVar()
        self.fine_label = Label(self.fine_frame,
                                textvariable= self.fine)
        self.fine_label.pack()
        # Create message display
        self.msg = StringVar()
        self.msg_label = Label(self.msg_frame,
                               textvariable= self.msg)
        self.msg_label.pack()
        # Create action & exit buttons
        self.calc_button = Button(self.bottom_frame,
                                  text= "Calculate Fine",
                                  command= self.calcFine)
        self.exit_button = Button(self.bottom_frame,
                                  text= "Exit",
                                  command= self.root.destroy)
        self.calc_button.pack()
        self.exit_button.pack()



    def calcFine(self):
        # Establish variables
        limit = float(self.limit_entry.get())
        speed = float(self.speed_entry.get())
        speedOver = speed - limit
        zoneVar = bool(self.zone_var.get())
        fineBracket = 0
        fineAmount = 0
        fineMessage = ""

        # Establish speed over limit brackets
        if speedOver <= 0:
            fineBracket = "None"
        if speedOver >= 5:
            fineBracket += 1
        if speedOver >= 15:
            fineBracket += 1
        if speedOver >= 25:
            fineBracket += 1
        if speedOver >= 30:
            fineBracket += 1

        # Determine the initial fine and display message
        if fineBracket == "None":
            fineAmount = 0
            fineMessage = "You are driving within the speed limit. Good job."
        if fineBracket == 0:
            fineAmount = 89
            fineMessage = "Slow down!"
        if fineBracket == 1:
            fineAmount = 129
            fineMessage = "Drive with caution!"
        if fineBracket == 2:
            fineAmount = 189
            fineMessage = "You are over speeding!"
        if fineBracket == 3:
            fineAmount = 279
            fineMessage = "You are in Danger zone!"
        if fineBracket == 4:
            fineAmount = "Fine determined in mandatory court."
            fineMessage = "See ya in court!!"

        # Apply zone to fine
        if zoneVar == True and fineBracket != 4:
            fineAmount = int(fineAmount) * 2
        if fineBracket != 4:
            fineAmount = "$" + str(fineAmount)
        self.fine.set(fineAmount)
        self.msg.set(fineMessage)
##        print(zoneVar, speedOver, "yay!", fineAmount, fineMessage)



##root.mainloop()

SpeedLimitGUI()

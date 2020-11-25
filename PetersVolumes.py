#File:    PetersVolumes.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.0 October 19, 2020

# This program finds the volumes of different 3D objects.


from math import pi

# displays options for user to choose from
def PetersMenu():
    print("""
    1.	Volume of a cube in cubic inches. 
    2.	Volume of a sphere in cubic inches. 
    3.	Volume of a cylinder in cubic inches.
    4.	Volume of a cone in cubic inches.
    5.	Exit the program.
    """)
    choice = int(input("Enter your choice: "))

# gets a valid input
    while choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=5:
        choice = int(input("Invalid Input. Enter your choice: "))

    print()
    if choice==1:
        cubeVolJoshua()
    if choice==2:
        sphereVolJoshua()
    if choice==3:
        cylVolJoshua()
    if choice==4:
        coneVolJoshua()
    if choice==5:
        print("Bye!")

# calculates the volume of a cube with valid inputs   
def cubeVolJoshua():
    print("We are going to calculate the volume of a cube.")
    a = float(input("Length of the side of the cube in inches: "))
    while validInput(a) == False:
        a = float(input("Invalid Input.\nPlease input a positive value for the \
Length of the side of the cube in inches: "))
    else:
        Vol = a**3
        print(f"The volume of the cube: {Vol:.2f} cubic inches")
        PetersMenu()

# calculates the volume of a sphere with valid inputs
def sphereVolJoshua():
    print("We are going to calculate the volume of a sphere.")
    r = float(input("Radius of the sphere in inches: "))
    while validInput(r) == False:
        r = float(input("Invalid Input.\nPlease input a positive value for the \
Radius of the sphere in inches: "))
    else:
        Vol = (4/3)*pi*r**3
        print(f"The volume of the sphere: {Vol:.2f} cubic inches")
        PetersMenu()

# calculates the cylinder of a cube with valid inputs   
def cylVolJoshua():
    print("We are going to calculate the volume of a cylinder.")
    r = float(input("Radius of the cylinder in inches: "))
    h = float(input("Height of the cylinder in inches: "))
    while validInput(r) == False:
        r = float(input("Invalid Input.\nPlease input a positive value for the \
Radius of the cylinder in inches: "))
    else:
        while validInput(h) == False:
            h = float(input("Invalid Input.\nPlease input a positive value for the \
Height of the cylinder in inches: "))
        else:
            Vol = pi*(r**2)*h
            print(f"The volume of the cylider: {Vol:.2f} cubic inches")
            PetersMenu()

# calculates the cone of a cube with valid inputs   
def coneVolJoshua():
    print("We are going to calculate the volume of a cone.")
    r = float(input("Radius of the cylider in inches: "))
    h = float(input("Height of the cylider in inches: "))
    while validInput(r) == False:
        r = float(input("Invalid Input.\nPlease input a positive value for the \
Radius of the cylider in inches: "))
    else:
        while validInput(h) == False:
            h = float(input("Invalid Input.\nPlease input a positive value for the \
Height of the cylider in inches: "))
        else:
            Vol = (1/3)*pi*(r**2)*h
            print(f"The volume of the cone: {Vol:.2f} cubic inches")
            PetersMenu()

# makes sure input is positive
def validInput(x):
    if x >= 0:
        return True
    else:
        return False
        
    

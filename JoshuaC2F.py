# File:    JoshuaC2F.py 
# Project: CSIS2101 Assignment 2
# Author:  Joshua Peters 
# History: Version 0.4 August 29, 2020

# This program will convert the unit of temperature Celsius into Fahrenheit


# Formalities/
print("Greetings, I will convert Celsius into Fahrenheit for you ;)")

# Get value from user/
JoshuaCel = float(input("What is the Celsius temperature you would like me to convert?"))

# Convert C to F/
ConvFar = JoshuaCel * 9 / 5 + 32 

# Display value to user/
print("That temperature in Fahrenheit is:", ConvFar)

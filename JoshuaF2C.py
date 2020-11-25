#File:    JoshuaF2C.py 
#Project: CSIS2101 Assignment 2
#Author:  Joshua Peters 
#History: Version 0.4 August 29, 2020

# This program will convert the unit of temperature Fahrenheit into Celsius


# Formalities/
print("Greetings, I will convert Fahrenheit into Celsius for you ;)")

# Get value from user/
JoshuaFar = float(input("What is the Fahrenheit temperature you would like me to convert?"))

# Convert F to C/
ConvCel = (JoshuaFar - 32) * 5 / 9

# Display value to user/
print("That temperature in Celcius is:", ConvCel)

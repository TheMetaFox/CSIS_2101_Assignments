#File:    rectangleJoshuaPeters.py 
#Project: CSIS2101 Participation 2
#Author:  Joshua Peters 
#History: Version 0.1 August 29, 2020

# This program calculates area and perimeter of a rectangle.

# Inputs - Length of the rectangle and Width of the rectangle
# Output is the area which length is multiplied by width and
#the perimeters which is double the sum of length and width.


# Find the dimensions/
length = float(input("What is the length of the rectangle?"))
width = float(input("What is the width of the rectangle?"))

# Calculate and store the area and perimeter/
area = length * width
perimeter = (length + width) * 2

# Print the result/
print("The area of the rectangle is", area, "and the perimeter is", perimeter)

# Alternate method using string concatination/
#  Calculate and store the area and perimeter as a string//
area = str(length * width)
perimeter = str((length + width) * 2)

#  Print the result//
print("The area of the rectangle is " + area + " and the perimeter is " + perimeter)

# Allow the .exe file to stay open; keeps the program running/
input("The area of the rectangle is " + area + " and the perimeter is " + perimeter)

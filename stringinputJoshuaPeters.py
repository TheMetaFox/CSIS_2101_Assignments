#File:    colorstringinput.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.1 September 3, 2020

# This program mixes primary colors and displays the sencondary color.

def main():

    # Display instructions for user/
    
    print("Hello, I will help you find the secondary color that is created from \
two different primary colors of your choosing. Please input the capital of the \
first letter of the color you chose(i.e. R, B, or Y).\n")

    # Get the two colors/

    pcolor1 = input("First color: ")
    pcolor2 = input("Second color: ")

    # Confirm values are valid/ 

    validColor = False

    if pcolor1 == "R" or pcolor1 == "B" or pcolor1 == "Y":
        validColor = True

    if validColor != True:
        input("Invalid Color")

    if pcolor1 == pcolor2:
        input("Same Color")
    
    # Mix the two primary colors/

    if pcolor1 == "R" and pcolor2 == "B":
        print("The secondary color is Purple.")
    if pcolor1 == "B" and pcolor2 == "R":
        print("The secondary color is Purple.")
    if pcolor1 == "R" and pcolor2 == "Y":
        print("The secondary color is Orange.")
    if pcolor1 == "Y" and pcolor2 == "R":
        print("The secondary color is Orange.")
    if pcolor1 == "Y" and pcolor2 == "B":
        print("The secondary color is Green.")
    if pcolor1 == "B" and pcolor2 == "Y":
        print("The secondary color is Green.")

main()

"""
    if ((pcolor1 == "R" or "B") and (pcolor2 == "R" or "B")):
        print("The secondary color is Purple.")

    if ((pcolor1 == "R" or "Y") and (pcolor2 == "R" or "Y")):
        print("The secondary color is Orange.")

    if ((pcolor1 == "Y" or "B") and (pcolor2 == "Y" or "B")):
        print("The secondary color is Green.")
"""

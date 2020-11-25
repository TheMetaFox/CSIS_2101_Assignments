#File:    Midterm12.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 September 26, 2020

# This program's functionis to advise the university on how many packets of masks to buy.

import math

x = int(input("Number of students: "))
y = x/5
print("You should buy", math.ceil(y), "packets of masks")

#File:    FishMain.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 November 5, 2020

# This program's function is...

from FishMainclass import Fish
"""
# Creat two objects
First one a Mahi mahi with weight = 3 pounts; length = 6 inches and price per\
unit = $3.00. Second one create an instance which is "Salmon" with length = 9
inches and weight = 5 pounds and ppu = $2.1
Print the details of each fish and compare the price and print out whether
salmon is costlier or Mahi mahi."""

def main():
    fish1 = Fish("Mahi mahi", 3, 6, 3.00)
    fish2 = Fish("Salmon", 9, 5, 2.10)

    fishPrice1 = fish1.calc_price(fish1.get_ppu())
    fishPrice2 = fish2.calc_price(fish2.get_ppu())

    if fishPrice1 > fishPrice2:
        print("The", fish1.get_name(), "is more costly than", fish2.get_name())
    if fishPrice2 > fishPrice1:
        print("The", fish2.get_name(), "is more costly than", fish1.get_name())



##fishNum = int(input("How many fish are you comparing? "))
##priceList = []
##              
##for i in range(fishNum):
##    fishName = input("Name: ")
##    fishWeight = float(input("Weight: "))
##    fishLength = float(input("Length: "))
##    fishPpu = float(input("Price Per Unit: "))
##    fish = Fish(fishName, fishWeight, fishLength, fishPpu)
##    fishPrice = fish.calc_price(fishPpu)
##    priceList.append(fishPrice)
##              
##print(priceList)

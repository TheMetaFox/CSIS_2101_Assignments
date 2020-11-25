#File:    menu.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.7 October 28, 2020

# This program finds the total amount to pay for different items.

"""
Create a txt file called menu.txt
Then have the following items in the menu.
Burger 10.99
Milkshake 3.99
Salads 2.99
Cookies 0.99
Applepie 2.99


Write a program called menu.py which
Replace Burger 10.99 with Hotdog 4.99
Find the total amount you need to pay for all these items."""

def main():
# open & establish menu list
    file = "menu.txt"
    menu = open(file,"w")
    menuList = ["Burger10.99","Milkshake 3.99","Salads$2.99",
                "Cookies $0.99","$2.99 Applepie"]


# writes list as is
    for i in range(len(menuList)):
        menu.write(menuList[i]+"\n")
        


# displays the information written in file 
    print("\nFile: " + file + "\nInput: ")
    print(createMenu(menuList))
    print(totalPrice(menuList))
    menu.write(createMenu(menuList))
    menu.write(totalPrice(menuList))


# replaces burger values with hotdog values
    newi = ""
    for i in menuList:
        if i.find("Burger") == 0:
            newi = i.replace("Burger", "Hotdog")
            newi = newi.replace("10.99", "4.99")
            menuList[menuList.index(i)] = newi



        
# displays the information written in file 
    print("\nFile: " + file + "\nInput: ")
    print(createMenu(menuList))
    print(totalPrice(menuList))
    menu.write(createMenu(menuList))
    menu.write(totalPrice(menuList))


    menu.close()
    print("\nDone")



def totalPrice(menuList):
# initializes, separates, & outputs item and price variables from menu list
    priceString = ""
    for item in menuList:
        for char in item:
            if char.isdigit() or char == ".":
                priceString +=  char
        priceString +=  "\n"
##    print(priceString)



# puts item and price values into respective lists
    priceList = priceString.rstrip("\n")
    priceList = priceList.split("\n")
    totalPrice = 0
    for i in priceList:
        totalPrice += float(i)
    display = f"The total price: {totalPrice:.2f}\n"
    return display

def createMenu(menuList):

# initializes, separates, & outputs item and price variables from menu list
    itemString = ""
    priceString = ""
    for item in menuList:
        for char in item:
            if char.isalpha():
                itemString += char
            if char.isdigit() or char == ".":
                priceString +=  char
        itemString += "\n"
        priceString +=  "\n"
##    print(itemString)
##    print(priceString)



# puts item and price values into respective lists
    itemList = itemString.rstrip("\n")
    priceList = priceString.rstrip("\n")
    itemList = itemList.split("\n")
    priceList = priceList.split("\n")
##    print(itemList)
##    print(priceList)


    menuInput = "\t"*2 + "Menu"
    i = 0
    for i in range(i,len(menuList)):       
#       print("\t", end= "")
        menuInput += ("\n\t")
        if len(itemList[i])< 8:
#           print(itemList[i] + "\t"*2 + priceList[i])
            menuInput += (itemList[i] + "\t"*2 + priceList[i])
        else:
#           print(itemList[i] + "\t" + priceList[i])
            menuInput += (itemList[i] + "\t" + priceList[i])          
#       print("i is at:", i)
        i += 1
    menuInput += "\n"
    return menuInput


#File:    JoshuaOrderReceiptList.py
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 November 10, 2020


"""
Using an list of item objects, instead of item1, item2, etc. Put item1 item2,
item3 and item4 in the list. For each item in the list call __str__() and
Use the list and the for loop to find the dTotalPrice and iTotalWeight as in
part A."""

import Item

def main():
    dTotalPrice = 0.0         
    iTotalWeight = 0

    item1 = Item.Item(9.99, 5, "Cloth Masks Packet")
    item2 = Item.Item(11.49, 27, "Hand Sanitizer")
    item3 = Item.Item(24.99, 15, "Head Shield") 
    item4 = Item.Item(8.91, 7, "Eye protection Goggles") 
    item4.set_quantity(2)   

    items = [item1, item2, item3, item4]

    print("Here are your shopping cart contents.")
    for item in items:
        print(item)
        dTotalPrice += item.get_order_price()
        iTotalWeight += item.get_order_weight_in_ounces()

    print("The price of your order is $"+ str(dTotalPrice))         
    print("The shipping weight is", (iTotalWeight // 16),
          "pounds", iTotalWeight % 16 , "ounces")     

#File:    PetersSpeedLimit.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.6 November 5, 2020

# This program calculates the speeding fine in different situations.


def PetersSpeedLimit():

    # Define them variables/
      # Validity variables/
    ValidZone = False

      # Inputed variables/
    speedLimitJoshua = int(input("What is the speed limit of the zone? "))
    speedJoshua = int(input("What was the speed of the vehicle? "))
    cOrSZoneJoshua = input("Is the zone school or construction? ")

      # Calculated variables/
    speedOverJoshua = (speedJoshua - speedLimitJoshua)
    fineBracket = 0
    fineAmount = 0
    fineMessage = ""

    # Check validity of cOrS variable/
    if cOrSZoneJoshua == "Yes" or cOrSZoneJoshua == "Y" or \
       cOrSZoneJoshua == "No"  or cOrSZoneJoshua == "N":
        ValidZone = True
    else:
        cOrSZoneJoshua = input("Please input either a Yes(Y) or No(N): ")
        if cOrSZoneJoshua != "Yes" and cOrSZoneJoshua != "Y" and \
           cOrSZoneJoshua != "No"  and cOrSZoneJoshua != "N":
            input("Invalid Input")
            cOrSZoneJoshua = "error"

    # Establish speed over limit brackets/
    if speedOverJoshua <= 0:
        fineBracket = "None"
    if speedOverJoshua >= 5:
        fineBracket += 1
    if speedOverJoshua >= 15:
        fineBracket += 1
    if speedOverJoshua >= 25:
        fineBracket += 1
    if speedOverJoshua >= 30:
        fineBracket += 1

    # Determine the initial fine and display message/
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

    # Apply cOrS to fine/
    if cOrSZoneJoshua == "error":
        fineAmount = "error"
    elif cOrSZoneJoshua == "Yes" or cOrSZoneJoshua == "Y" and \
        fineAmount != str(fineAmount):
        fineAmount = fineAmount * 2

    # Display all information/
    print("\n")
    print("Speed Limit:", speedLimitJoshua)
    print("Vehicle Limit:", speedJoshua)
    print("Construction or School Zone:", cOrSZoneJoshua)
    if fineAmount == "error":
        print("Can't calculate fine amount.")
    elif fineAmount == str(fineAmount):
        print(fineAmount)
    else:
        print(f"Total Fine Amount: ${fineAmount:.2f}")
    input(fineMessage)

"""
    print("\n")
    print(speedOverJoshua)
    print(fineBracket)
"""    

PetersSpeedLimit()

#File:    AHSPeters.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.0 September 26, 2020

# This program's function plays Rock Paper and Scissors using comic characters.

import random

def AHSPeters():
# introduces the program and its function \
    print("Welcome to my special version of Rock Paper Scissors. This game \
uses the comic book characters Aquaman, Human Torch, and Swamp Thing instead. \
Aquaman beats Human Torch, Human Torch beats Swamp Thing, and Swamp Thing \
beats Aquaman.")
    print()

    # asks user for imput and if it's invalid, another one \
    user = input("Input 'A' for Aquaman, 'H' for Human Torch, or 'S' \
for Swamp Thing: ")
    while user != "A" and user != "H" and user != "S":
        user = input("Invalid Input. Please input 'A', 'H', or 'S': ")


    janken(playUser(user),playComp())


def janken(user,comp):
    print()
    print("You:",user)
    print("Computer:",comp)

    if user == comp:
        user = playUser(input("Tie, please play again and input 'A', 'H', or \
'S': "))
        comp = playComp()
        janken(user,comp)
    elif user == "Aquaman":
        if comp == "Human Torch":
            input("You win! Aquaman extinguishes Human Torch!")
        if comp == "Swamp Thing":
            input("You lose! Swamp Thing drowns Aquaman!")
    elif user == "Human Torch":
        if comp == "Swamp Thing":
            input("You win! Human Torch burns Swamp Thing!")
        if comp == "Aquaman":
            input("You lose! Aquaman extinguishes Human Torch!")
    elif user == "Swamp Thing":
        if comp == "Aquaman":
            input("You win! Swamp Thing drowns Aquaman!")
        if comp == "Human Torch":
            input("You lose! Human Torch burns Swamp Thing!")

# randomizes computers response \
def playComp():
    global comp
    cpu = random.randrange(100,300+1,100)
    if cpu == 100:
        comp = "Aquaman"
    elif cpu == 200:
        comp = "Human Torch"
    else:
        comp = "Swamp Thing"
    return comp

def playUser(user):
    if user == "A":
        user = "Aquaman"
    elif user == "H":
        user = "Human Torch"
    else:
        user = "Swamp Thing"
    return user

AHSPeters()

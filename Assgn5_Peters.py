#File:    Assgn5_Peters.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 September 18, 2020

# This program prints the lyrics to the song "Old McDonald" and octothorps

def main():
    animal = "cow"
    sound = "moo"
    joshuaNurseryRhyme(animal,sound)

    animal = "chick"
    sound = "cluck"
    joshuaNurseryRhyme(animal,sound)

    animal = "pig"
    sound = "oink"
    joshuaNurseryRhyme(animal,sound)

    petersPoundSign()
    
def joshuaNurseryRhyme(animal,sound):
    print(f"""
    Old Macdonald had a farm, E-I-E-I-O
    And on his farm he had a {animal}, E-I-E-I-O
    With a "{sound}-{sound}" here and a "{sound}-{sound}" there
    Here a "{sound}" there a "{sound}"
    Everywhere a "{sound}-{sound}"
    Old Macdonald had a farm, E-I-E-I-O
    """)


def petersPoundSign():
    n = int(input("Enter number of rows: "))
    row = 0
    
    for n in range(1,n+1):
        while row < n:
            print("",end= "#")
            row += 1
        print("")
        row = 0

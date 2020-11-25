#File:    whilesumdemoPeters.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.0 September 10, 2020

# You are given a positive number n.
# Find the sum of the first n numbers using a while loop.
# If n = 3 sum shoub be 6 or if n = 10 sum should be 55.



def forloop():
    n = int(input("To what number shall I calculate the partial sum?"))
    sumNum = 0
    for num in range(n+1):
        sumNum = sumNum + num

    print("Sum of", n, "numbers is", sumNum)


def main():
    n = int(input("To what number shall I calculate the partial sum?"))
    sumNum = 0
    counter = 1
    while counter <= n:
        sumNum = sumNum + counter
        counter += 1

    print("Sum of", n, "numbers is", sumNum)


def main1():
    n = int(input("To what number shall I calculate the partial sum?"))
    sumNum = 0
    counter = 0
    while counter in range(n+1):
        sumNum = sumNum + counter
        counter += 1

    print("Sum of", n, "numbers is", sumNum)


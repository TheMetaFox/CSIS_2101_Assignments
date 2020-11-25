#File:    PetersLoops.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.0 September 11, 2020


 #  1. Write a loop that counts from 10 down to 1 skipping, printing the count
## value each time in the loop. The output should look like (notice the spacing):
## 10 9 8 7 6 5 4 3 2 1 Call this loop within loops().

def loops():
    x = []
    for counter in range(10,0,-1):
        x.append(counter)
#        print(counter)
    print(*x)



 #  2. Write a loop that counts from 3 to 30 by threes, printing the count in
## each iteration. The output should look like: 3,6,9,12,15,18,21,24,27,30
## Notice the commas. Notice that there is no comma at the beginning or end.
## That means that you must do something special either at the beginning or at
## the end.

    x = []
    for counter in range(3,31,3):
        x.append(counter)
#        print(counter)
    print(*x, sep= ",")

 #  3. Ask the user to input an integer parameter The loop should count down
## only the even numbers, starting with the input number and ending with 0.
## For this you should use a while loop. The numbers should all appear on the
## same line. 
##
## So for example if the input number passed is 10 (an even number) the output
## should be: 10 8 6 4 2 0
##
## So for example if the input number passed is 11 (an odd number) the output
## should be : 10 8 6 4 2 0

    start = int(input("What number would you like to start counting down from?"))
    if start % 2 != 0:
        start -= 1
    x = []
    for counter in range(start,-1,-2):
        x.append(counter)
#        print(counter)
    print(*x)    
        

 #  4. Ask the user to input an integer parameter. The loop should count up all
## the odd numbers below the number, starting with the number 1 and up to the
## number that was passed as the input parameter. For this you should use a for
## loop. The numbers should all appear on the same line. 
##
## So for example if the number passed in using input is 7 the output should be: 
## 1 3 5 7

    end = int(input("What number would you like to start counting up from?"))
    if end % 2 != 1:
        end -= 1
    x = []
    for counter in range(1,end+2,2):
        x.append(counter)
#        print(counter)
    print(*x)

#File:    ListFunctionsJoshua.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 1.0 October 24, 2020

# This program outputs a set of values that pertain to a user's list.

"""
# Within your main function, create an empty list and using a loop append
10 numbers input by the user to the list. The program should then call each
of the functions provided above by passing in the list you created as an
argument. Except for the median, where you make a deep copy of the list and
pass that list and not the original list. And then display the return values
within this firstNameList() with meaningful messages."""
def joshuaList():
    userLen = int(input("Desired length of list: "))
    userList = []
    for i in range(1,userLen+1):
        userList.append(int(input(f"Input value #{i}: ")))
    clipNum = int(input("Number you'd like to clip list at: "))
    print("Given List: ", userList)
    print("Range of the List: ", rangeList(userList))
    print("Sum of the List: ", sumList(userList))
    print("Average of the List: ", average(userList))
    print("Median of the List: ", median(userList))
    print("Clipped List at", clipNum, "is: ", *clip(userList, clipNum))



"""
# returns range of the list. Range is largest number in the list – the
smallest number in the list. You can use already available functions max and
min on a list. So if the largest number is 13 and smallest number in the list
is 5, then return 8 (which is 13 – 5)."""
def rangeList( number_list ):
    maxNum = max(number_list)
    minNum = min(number_list)
    rangeNum = maxNum - minNum
    return rangeNum



"""
# returns the sum of the numbers in the list. In this function write your own
program by using  a for loop to find the sum of the numbers. Once you find
the sum using your method check whether the sum you found is equal to the
available function sum on a list."""
def sumList( number_list ):
    sumNum = 0
    for i in number_list:
        sumNum += i
    return sumNum



"""
# returns mean or average. Use the sumList (..) function(previous fn) to
calculate the average."""
def average( number_list ):
    sumNum = 0
    for i in number_list:
        sumNum += i
    meanNum = sumNum / len(number_list)
    return meanNum



"""
# returns median of the list. Median is the middle number of the list after
the list is sorted in ascending order. If numbers are even, median is the
average of the two middle numbers. You can use the available function sort
to sort the numbers."""
def median( number_list ):
    mutabiList = number_list.copy()
    medianNum = 0
    if len(mutabiList) % 2 == 0:
        for i in range(int(len(mutabiList)/2)-1):
            mutabiList.remove(max(mutabiList))
            mutabiList.remove(min(mutabiList))
        sumNum = 0
        for i in mutabiList:
            sumNum += i
        medianNum = sumNum/2
    else:
        for i in range(int(((len(mutabiList))-1)/2)):
            mutabiList.remove(max(mutabiList))
            mutabiList.remove(min(mutabiList))
        medianNum = mutabiList[0]
    return medianNum




"""
# returns the clipped array based on the clipNum. Clipping an array is
replacing all the numbers greater than the number provided to that number.
So for example if the list is [3,17,5,9,1,11] and the clipNum is 8, returned
array is [3,8,5,8,1,8]. So all numbers greater than the clipNumber (here 8)
is replaced by the clipNum(which is 8 in this example). clipNum that takes a
maximum value as an argument and changes any value in the list that is higher
than the specified maximum value to be the same as the maximum value. This
function could also be called “haircut”, in that it takes values that are
too high, and cuts them down to the maximum allowable height. (Think of a
scissor going through your hair and trimming the ones that are too long.)"""
def clip( number_list, clipNum ):
    clippedList = number_list.copy()
    for i in clippedList:
        if i > clipNum:
            clippedList[clippedList.index(i)] = clipNum
    return clippedList


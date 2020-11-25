#File:    Assgn9peters.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 September 26, 2020

# This program's function is to...

def main():
    jSReplace()
    jSNumberConverter()
    jSPigLatin()
"""
# In Python operation on strings when you use replace(oldstring, new string)
function all the old strings are replaced by the new string. We did in our
participation problem the first instance of the old string being replaced with
the new string. But write your own Replace function which replaces just the
last instance of the old string with the new string. In this problem you dont
want to replace all old strings with a new string. But just the last instance
of that string.
# For example The input string is "Mississippi" Old String to be replaced is
"ss" and has to be replaced with "zz", only the last ss is replaced and not
all ss. Output is "Missizzippi" """
def jSReplace():

# assigns user inputs as variables
    userString = input("Input string: ")
    oldString = input("Input old string: ")
    newString = input("Input new string: ")

# assigns the reverse to new variables
    revuserString = reverse(userString)
    revoldString = reverse(oldString)
    revnewString = reverse(newString)

# replaces the first occurance reversed, making it the last
    newuserString = revuserString.replace(revoldString, revnewString, 1)

# displays the re-reversed string
    print("Your new string:", reverse(newuserString))

# returns the reverse of the string argument
def reverse(str):
    newstr = ""
    for char in str:
        newstr = char + newstr

    return newstr




"""
Write a program that asks the user to enter a 10 character telephone number in
the format XXX-XXX-XXXX or a 7 character telephone number in the format
XXX XXXX (In both formats with or without the hyphen “-“). You don’t have to
validate the format. It can be all alphabets or mixture of alphabet and
Numbers. The application should display the telephone number with any
alphabetic character that appeared in the original translated into their
numeric equivalent. """
def jSNumberConverter():

# assign user inputed number to variable
    teleUser = input("Enter telephone number: ")
    teleNum = ""

# converts letters into numbers
    for char in teleUser:
        if char.isalpha() == True:
            char = char.upper()
            if char == "A" or char == "B" or char == "C":
                teleNum += "9"
            if char == "D" or char == "E" or char == "F":
                teleNum += "8"
            if char == "G" or char == "H" or char == "I":
                teleNum += "7"
            if char == "J" or char == "K" or char == "L":
                teleNum += "6"
            if char == "M" or char == "N" or char == "O":
                teleNum += "5"
            if char == "P" or char == "Q" or char == "R" or char == "S":
                teleNum += "4"
            if char == "T" or char == "U" or char == "V":
                teleNum += "3"
            if char == "W" or char == "X" or char == "Y" or char == "Z":
                teleNum += "2"
        else:
            teleNum += char

# diplay new number
    print("Converted number:", teleNum)







"""
Write a program that accepts a sentence as an input and converts each word to
pig latin. In this version to covert a word into pig latin, you remove the
last letter of each word and place that letter at the beginning of the word.
Then you append the string ‘XX’ to the word. Here is an example:
English:   	I SLEPT MOST OF THE NIGHT.
Pig Latin: 	IXX TSLEPXX TMOSXX FOXX ETHXX TNIGHXX
The program should handle upper case and lower case alphabets. """
def jSPigLatin():
# assigns user input to variable
    userEng = input("Input english text to be converted: ")

# separates the words of user input and assigns it to variable
    listEng = userEng.split()

# establishing global variable
    listPig = ""

# iterates through each word
    for word in listEng:

# turns word into list with each character separate
        listChar = list(word)

# takes the last character and puts it in the front and adds "XX" at the end
        last = word[len(word)-1]
        del listChar[len(word)-1]
        listChar.insert(0, last)
        listChar.append("XX")

# adds the end product of the word iteration to the variable of final output
        for i in listChar:
            listPig += i
        listPig += " "
            
# displays output
    print("Pig Latin Translation:", listPig)




    

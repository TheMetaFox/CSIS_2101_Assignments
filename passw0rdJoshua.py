#File:    passw0rdJoshua.py 
#Project: CSIS2101 
#Author:  Joshua Peters 
#History: Version 0.0 November 2, 2020

# This program reads a set of passwords from a file, checks if the password meets
#criteria, then output that information into an output file.



"""
  Create a python file passw0rdFirstName. The main() should read in the given
input file passwdin.txt. This input file has six passwords. Your main method
should read each password and call the above method with each string as the
argument and write the password string and the return message into an output
file firstnamepasswdout.txt."""
def main():
    psswdFile = open("passwdin.txt","r")
    msgFile = open("joshuapasswdout.txt","w")
    psswdList = psswdFile.readlines()
    for psswd in psswdList:
        psswd = psswd.rstrip("\n")
        msgFile.write(checkPassw0rdJoshua(psswd))
        print(checkPassw0rdJoshua(psswd))

    psswdFile.close()
    msgFile.close()
    
"""
  The password uses the following criteria:
•   The password should be at least 8 characters strong. 
•   The password should contain at least TWO upper case letters.
•   The password should contain at least TWO lower case letters
•   The password should have at least one digit.
•   The password should have no special characters like $ or ! or % or space. 
  The function then verifies that it meets the stated criteria. If it does it
should return message “Password Accepted”. If not it should return a message as
to what is wrong with the password and why it is not accepted."""
def checkPassw0rdJoshua(psswd):
    message = psswd + " -- "
    psswdLen, psswdUp, psswdLow, psswdDig, psswdSpe = 0, 0, 0, 0, 0
    try:
        for char in psswd:
            if char.isalnum() == True:
                psswdLen += 1
                if char.isupper() == True:
                    psswdUp += 1
                if char.islower() == True:
                    psswdLow += 1
                if char.isdigit() == True:
                    psswdDig += 1
            else:
                psswdSpe += 1

        if psswdLen < 8 or psswdUp < 2 or psswdLow < 2 or\
           psswdDig < 1 or psswdSpe > 0:
            message += "Password Not Accepted"
        else:
            message += "Password Accepted"

        if psswdLen < 8:
            message += "\nPassword must be at least 8 characters long."
        if psswdUp < 2:
            message += "\nPassword must have at least 2 upper case letters."
        if psswdLow < 2:
            message += "\nPassword must have at least 2 lower case letters."
        if psswdDig < 1:
            message += "\nPassword must have at least 1 digit."
        if psswdSpe > 0:
            message += "\nPassword must not have any special characters."
    except:
        message += "Error"
    finally:
        message += "\n\n"
    
    return message

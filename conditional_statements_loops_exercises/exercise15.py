# 15. Write a Python program to check the validity of passwords input by users.
import re
password=input("Enter the password :")
x=True
while x:
    if len(password)<6 or len(password)>12:
        break
    elif not re.search("[a,z]",password):
        break
    elif not re.search("[A,Z]",password):
        break
    elif not re.search("[0,9]",password):
        break
    elif not re.search("[$#@]",password):
        break
    elif not re.search("/s",password):
        break
    else:
        print("You have entered  correct password ")
        x=False
        break
    
if x:
    print("Not valid password")    
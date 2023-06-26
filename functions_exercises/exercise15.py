# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.

def SorterWithLetter(string):
    x=string.split()
    x.sort()
    sorted_string=" "
    for sorted in x:
        sorted_string+=sorted
        sorted_string+=" "
    print(sorted_string)    
       
SorterWithLetter("hello my name is dilshod ")      
# >>>dilshod hello is my name  


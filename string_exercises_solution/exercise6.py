# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
word=input('Enter the word:')
x=len(word)
if x>3:
    if word[-3:]=='ing':
        print(word.replace('ing','ly'))
    else:
        print(word+"ing")    


#>>> Expected Result
#>>> Enter the word:helloing
#>>> helloly

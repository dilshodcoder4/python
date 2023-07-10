# 4. Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', except the first char itself
# initializing string
word= 'redaprle'
print("The original string is : " + str(word))
 
A = '$'
b=""
for i in word:
    if i==word[0] and i not in b:
        b+=i
    elif i==word[0] and i in b:
        b+=A
    else:
        b+=i
print("Replaced String : " + str(b))

# Expected Result
# Replaced String : redap$le

# 1. Write a Python program to calculate the length of a string.
# def calculate_length_of_string(strr):
#     print(len(strr))
# calculate_length_of_string('dilshod')    

#Expected Result
#>>> 7

# # 2. Write a Python program to count the number of characters (character frequency) in a string.
# word=input("Enter word :")
# x=len(word)
# for n in range(x):
#     print(f'{word[n]} >>> {word.count(word[n])}')

#Expected Result
#>>>  e >>> 3
#>>>  x >>> 1
#>>>  e >>> 3
#>>>  r >>> 1
#>>>  c >>> 1
#>>>  i >>> 1
#>>>  s >>> 2
#>>>  e >>> 3
#>>>  s >>> 2    
   

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string
# def swapcharr(string):
#     if len(string)>2:
#         print(f'{string[:2]}{string[-2:]}')
#     elif len(string)==2 :
#         print(string*2)       
#     else:
#         return ''

# swapcharr('he')
# swapcharr('hello')
# swapcharr('h')

#Expected Result
# >>>hehe
# >>>helo


#4. Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', except the first char itself
# initializing string
# word= 'redaprle'
# print("The original string is : " + str(word))
 
# A = '$'
# b=""
# for i in word:
#     if i==word[0] and i not in b:
#         b+=i
#     elif i==word[0] and i in b:
#         b+=A
#     else:
#         b+=i
# print("Replaced String : " + str(b))

#Expected Result
# Replaced String : redap$le

# 5. Write a Python program to get a single string from two given strings,
#  separated by a space and swap the first two characters of each string.
# word1=input('Enter first word:')
# word2=input('Enter second word:')
# print(f'{word1.replace(word1[:2],word2[:2])} {word2.replace(word2[:2],word1[:2])}')

#Expected Result
#>>> Enter first word:dello
#>>> Enter second word:dilshod
#>>> dillo delshod

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
# word=input('Enter the word:')
# x=len(word)
# if x>3:
#     if word[-3:]=='ing':
#         print(word.replace('ing','ly'))
#     else:
#         print(word+"ing")    


#>>> Expected Result
#>>> Enter the word:helloing
#>>> helloly



# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# def not_poor(word):
#   snot = word.find('not')
#   spoor =word.find('poor')
  

#   if spoor > snot and snot>0 and spoor>0:
#     word = word.replace(word[snot:(spoor+4)], 'good')
#     return word
#   else:
#     return word
# print(not_poor('Mr Thomas is not that poor!'))

#>>> Mr Thomas is good!
   

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one
# def return_lengh_of_value(a):
#     return len(a)

# word=input('Enter the word :')
# x=word.split()
# b=len(x)
# x.sort(key=return_lengh_of_value)
# print(x)
# print(x[b-1])

# 9. Write a Python program to remove the nth index character from a nonempty string. 
# word=input('Enter the word :')
# n=int(input("Which index character that you want to change"))
# print(word.replace(word[n],''))


#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]


word=input('Enter the word : ')      
change_sring(word)
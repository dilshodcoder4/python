
# 1. Write a Python program to calculate the length of a string.
# def calculate_length_of_string(strr):
#     print(len(strr))
# calculate_length_of_string('dilshod')    

#Expected Result
# #>>> 7

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

# #Expected Result
# #>>>hehe
# #>>>helo


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
# #>>> Enter first word:dello
# #>>> Enter second word:dilshod
# #>>> dillo delshod

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
# word=input('Enter the word:')
# x=len(word)
# if x>3:
#     if word[-3:]=='ing':
#         print(word.replace('ing','ly'))
#     else:
#         print(word+"ing")    


# #>>> Expected Result
# #>>> Enter the word:helloing
# #>>> helloly



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

# #>>>['is', 'boy', 'good', 'dilshod']
# #>>>dilshod



# 9. Write a Python program to remove the nth index character from a nonempty string. 
# word=input('Enter the word :')
# n=int(input("Which index character that you want to change :"))
# print(word.replace(word[n],''))

#>>> Enter the word :dilshod is bad guy
#>>> Which index character that you want to change :2
#>>> dishod is bad guy

#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
# def change_string(str1):
#       return str1[-1:] + str1[1:-1] + str1[:1]

# word=input('Enter the word : ')      
# print(change_string(word))

# #>>> Enter the word : hello
# #>>> oellh

# 11. Write a Python program to remove characters that have odd index values in a given string.
# def odd_element_change(word):
#     excepted_word = ""
#     for x in range(len(word)):
#         if x %2 == 0:
#             excepted_word=excepted_word + word[x]
#     return excepted_word

# WordToChange=input("Enter the word :")
# print(odd_element_change(WordToChange))      

# #>>> Enter the word :dilshodbek
# #>>> dlhde


# 12. Write a Python program to count the occurrences of each word in a given sentence
# def count_words(str):
#     counts=dict()
#     words=str.split()


#     for word in words:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1
#     return counts


# wordi=input("Enter the word :")
# print(count_words(wordi))


# #>>> Enter the word :hello how are you 
# #>>> {'hello': 1, 'how': 2, 'are': 1, 'you': 3}


# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# This question seemed so easy for me then i decided to code of swapcase() 
# def upper_lover(string):
#     empty_string=""
#     x=len(string)
#     for i in range(x):
#         if string[i] ==(string[i]).upper():
#             empty_string=empty_string+(string[i]).lower()
#         else:
#             string[i] ==(string[i]).lower()
#             empty_string=empty_string+(string[i]).upper()     
#     print(empty_string)


# upper_lover("hElo DilsHod")    
 
# #>>> HeLO dILShOD


#14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically)
# itmes = input("Input  words :")
# words = [word for word in itmes.split(",")]
# print(",".join(sorted(list(set(words)))))

#>>> Input  words :hello,is,dilshdo
#>>> dilshdo,hello,is


# 15. Write a Python function to create an HTML string with tags around the word(s)
# print("""Choose Tag :
# 1) <i> </i>
# 2) <b> </b>""")
# choise=int(input(""))
# word=input("Imput word :")

# if choise==1:
#     print(f'<i>{word}</i>')
# else:
#     print(f'<b>{word}</b>')

# #>>>   Choose Tag :
#  #>>>1) <i> </i>
#  #>>>2) <b> </b>
#  #>>>1
#  #>>>Imput word :hello how are you
#  #>>><i>hello how are you</i>


# # 16. Write a Python function to insert a string in the middle of a string
# print("""Choose Tag :
# 1)[[]]
# 2){{}}
# 3)<<>> """)
# choise=int(input("==> :"))
# word=input("Imput word :")
# if choise==1:
#     print(f"[[{word}]]")
# elif choise==2:
#     print("{{"+f"{word}"+"}}")
# else:
#     print(f"<<{word}>>")

# #>>>Choose Tag :
# #>>> 1)[[]]
# #>>>2){{}}
# #>>>3)<<>> 
# #>>>==> :3
# #>>>Imput word :hello world
# #>>> <<hello world>>


# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
# word=input("Imput the word :")
# if len(word)<2:
#     print("Please try again")
# else:    
#     print(word[-2:]*4)

# #>>> Imput the word :dilshod
# #>>> odododod

# # 18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# def take_three_elemnts(str):
#     if len(str)<3:
#         return str
#     else:
#         print(str[:3])    

# take_three_elemnts("hello")
# #>>>hel

# # 19. Write a Python program to get the last part of a string before a specified character.
# word=input("Imput word:")
# word2=word.split()
# word3=word2[:-1]
# empty_string=""
# for x in word3:
#     empty_string=empty_string+x

# print(empty_string)
# #>>>Imput word:hewll kjfdgksd fdjgkg
# #>>>hewllkjfdgksd


# # 20. Write a Python function to reverse a string if its length is a multiple of 4.
# def reverse_string(wrd):
#     if len(wrd)%4==0:
#         print(wrd[::-1])
#     else:
#         print(wrd)

# word=input("Imput the word : ")
# reverse_string(word)            

# #>>>Imput the word : hellodiy
# #>>>yidolleh

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
word=input("Imput the string : ")
word2=word[:4]
if word2[0]==(word2[0]).upper() and word2[1]==(word2[1]).upper():
    print(word.upper())
elif word2[0]==(word2[0]).upper() and word2[2]==(word2[2]).upper():
    print(word.upper())
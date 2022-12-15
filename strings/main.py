#Very often in our programmes, we will be dealing with numbers but almost as often,if not more  we will want to deal with text
#For example the user will be giving us some text  and we will be doing some processing on it  as well as we will be waiting some text out to the screen 
#And that is where the next datatype comes in In python  we have got another type called strings that are used to contain text like characters
# my_string='Hello world'
# print(my_string)
# #Hello world

# # <<<------------>>>
# string_with_quotes="Hello   it is me "
# another_with_quotes='he said "you are good boy"  !'
# multiline =""" Hello world
# My name is Dilshod 
# """
# print(multiline)
# # >>>   Hello world
# # My name is Dilshod

# #The + Operator
# # <<<------------>>>
# a="Hello"
# b="Dilshod"
# c="How are you "
# greeting=a + b + c
# print(greeting)
# #>>>Hello Dilshod How are you 
# # The * Operator
# c='you '
# v='me'
# d='we'
# print(c*4)
# #>>>youyouyouyou
# # The in Operator
# s='hello'
# b='hello world how are you '
# print('hello ' in b )
# print(s in b)
# # >>>True
# # >>>True
# # There is also a not in operator, which does the opposite:
# s='hello'
# b='hello world how are you '
# print('hello '  not in b )
# print(s not in b)
# #>>> False
# #>>> False

# # <<<------------>>>
# name= 'Jane'
# greeting='hello'+name
# print(greeting)
# #>>>hello Jane

# # <<<------------>>>
# age="25"
# print("you are "+age)
# #>>>  you are 25
# age_as_str=str(age)
# print("You are "+ age_as_str)
# #>>>  You are 25

# # <<<------------>>>
# age=25
# print(f"You are {age}")
# #>>>  You are 25

# # <<<------------>>>
# name="Dilshod"
# greeting=f"How are you {name}"
# print(greeting)
# #>>> How are you Dilshod

# # <<<------------>>>
# name="Dilshod"
# final_greeting="How are you {}"
# dilshod_greeting=final_greeting.format(name)
# print(dilshod_greeting)
# #>>> How are you Dilshod

# # <<<------------>>>
# name="Javlon"
# dilshod_greeting=final_greeting.format(name)
# print(dilshod_greeting)
# #>>> How are you Javlon

# # <<<------------>>>
# name="Dilshod"
# final_greeting="How are you {name}"
# dilshod_greeting=final_greeting.format(name="Dilshod")
# print(dilshod_greeting)
# #>>> How are you Dilshod

# # <<<------------>>>
# name=input("Enter your name :")
# final_greeting="How are you {name}"
# dilshod_greeting=final_greeting.format(name=name)
# print(dilshod_greeting)
# #>>> Enter your name : Dilshod
# #>>> How are you Dilshod
# # Getting user input in Pyhton 
# first_name="Tom"
# friend_name=input("Enter your friend name : ")
# print(f"Hello {first_name}.My friend name is {friend_name}")
# #>>> Enter your  friend name : Javlon
# #>>> Hello Tom .My friend name is Javlon

# # <<<------------>>>
# age=input('Enter your age :')
# age_num=int(age)
# print(f"You have lived for {age_num*12} months")
# #>>>Enter your age :4
# #>>>You have lived for 48 months

# # <<<------------>>>
# age=int(input('Enter your age :'))
# print(f"You have lived for {age*12} months")
# #>>>Enter your age :4
# #>>>You have lived for 48 months

# # <<<------------>>>
# age=int(input('Enter your age :'))
# months=age*12
# print(f"You have lived for {months} months")
# #>>>Enter your age :4
# #>>>You have lived for 48 months
# # Built-in String Functions

# # <<<------------>>>
# # chr()---->>> 	Converts an integer to a character
# # chr() does the reverse of ord(). Given a numeric value n 
# # chr(n) returns a string representing the character that corresponds to n:
# print(chr(97))
# #>>> 'a'

# # <<<------------>>>
# # ord()---->>> Returns an integer value for the given character.
# print(ord("a"))
# #>>> 97

# # <<<------------>>>
# #len()---->> Returns the length of a string
# greeting='i am Dilshodbek.I am 12 years old'
# print(len(greeting))
# #>>> 33

# # <<<------------>>>
# # str()---->>> Returns a string representation of an object
# print(str(66.6))
# #>>>'66.6'

#String indexing 
s='dilshod'
print(s[3])
#>>> s
print(s[2])
#>>> l
print(s[6])
#>>> d
print(len(s))
#>>> 7
print(s[len(s)-2])
#>>> o

# <<<------------>>>
# String indices can also be specified with negative numbers, in which case indexing occurs from the end of the string 
# backward: -1 refers to the last character, -2 the second-to-last character, and so on. Here is the same diagram showing both 
# the positive and negative indices into the string 'dilshod':
s='sanjar'
# -7=d
# -6=i
# -5=l
# -4=s
# -3=h
# -2=o
# -1=d
print(s[-1])
#>>> d
print(s[2:])
#>>> njar
print(s[:2]+s[2:])
#>>> sanjar
print(s[::3])
#>>> sj
t=s[:]
print(id(t))
#>>>140399892276080
print(id(s))
#>>>140399892276080
print(s is t)
#>>> True

























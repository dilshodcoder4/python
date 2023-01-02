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
#>>>Enter your age :4
#>>>You have lived for 48 months
# Built-in String Functions

# <<<------------>>>
# chr()---->>> 	Converts an integer to a character
# chr() does the reverse of ord(). Given a numeric value n 
# chr(n) returns a string representing the character that corresponds to n:
print(chr(97))
#>>> 'a'

# <<<------------>>>
# ord()---->>> Returns an integer value for the given character.
print(ord("a"))
#>>> 97

# <<<------------>>>
#len()---->> Returns the length of a string
greeting='i am Dilshodbek.I am 12 years old'
print(len(greeting))
#>>> 33

# <<<------------>>>
# str()---->>> Returns a string representation of an object
print(str(66.6))
#>>>'66.6'

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

# <<<------------>>>
#This is a common paradigm for reversing a string:
greeting="Hello learner how are you"
print(greeting[::-1])
#>>> uoy era woh renrael olleH


# <<<------------>>>
#Interpolating Variables Into a String
dilshod_apple=5
omadbek_apple=6
all_apples=dilshod_apple*omadbek_apple
print('Dilshod has',dilshod_apple,'apples,','Omadbek has',omadbek_apple,'apples,  and they have',all_apples,'apples in total.')
#>>> Dilshod has 5 apples, Omadbek has 6 apples,  and they have 30 apples in total.


# <<<------------>>>
#Recast using an f-string, the above example looks much cleaner:
dilshod_apple=5
omadbek_apple=6
all_apples=dilshod_apple*omadbek_apple
print(f'Dilshod has {dilshod_apple} apples,Omadbek has {omadbek_apple} apples,  and they have {all_apples} apples in total.')
#>>> Dilshod has 5 apples,Omadbek has 6 apples,  and they have 30 apples in total.


# <<<------------>>>
# There is also a built-in string 
name='dilshod'
print(name.replace('d','b'))
#>>> bilshob


# <<<------------>>>
# Case Conversion
# Methods in this group perform case conversion on the target string.

# <<<------------>>>
# capitalize() - Capitalizes the target string.
# capitalize() returns a copy of my_self with the first character converted to uppercase and all other characters converted to lowercase:
my_self="hello my name is dilshod"
print(my_self.capitalize())
#>>> Hello my name is dilshod

# <<<------------>>>
# lower() - Converts alphabetic characters to lowercase.
# lower() returns a copy of my_self with all alphabetic characters converted to lowercase:
my_self="Hello my name is Dilshod"
print(my_self.lower())
#>>>hello my name is dilshod



# <<<------------>>>
# swapcase() - Swaps case of alphabetic characters.
# swapcase() returns a copy of my_self with uppercase alphabetic characters converted to lowercase and vice versa:
my_self="Hello my name is Dilshod"
print(my_self.swapcase())
#>>>hELLO MY NAME IS dILSHOD


# <<<------------>>>
# title() - Converts the target string to “title case.”
# title()  returns a copy of my_self in which the first letter of each word is converted to uppercase and remaining letters are lowercase:
my_self="Hello my name is Dilshod"
print(my_self.title())
#>>>Hello My Name Is Dilshod
 

# <<<------------>>>
# upper() - Converts alphabetic characters to uppercase.
# upper()  returns a copy of my_self with all alphabetic characters converted to uppercase:
my_self="Hello my name is Dilshod"
print(my_self.upper())
#>>>HELLO MY NAME IS DILSHOD
 

#Find and Replace
# These methods provide various means of searching the target string for a specified substring.

# <<<------------>>>
# count() - Counts occurrences of a substring in the target string.
# count()  returns the number of non-overlapping occurrences of substring <sub> in my_self :
my_self="Hello my name is Dilshod"
print(my_self.count('i'))
#>>> 2
print(my_self.count('l'))
#>>> 3

# <<<------------>>>
# endwith() - Determines whether the target string ends with a given substring.
# endwith()   returns True if my_self ends with the specified <suffix> and False otherwise:
my_self="Hello my name is Dilshod"
print(my_self.endswith('Dilshod'))
#>>> True
print(my_self.endswith('name'))
#>>> False

# <<<------------>>>
# find() - Searches the target string for a given substring.
# find()  You can use .find() to see if a Python string contains a particular substring. my_self.find(<sub>) 
# returns the lowest index in my_self where substring <sub> is found:
my_self="Hello my name is Dilshod"
print(my_self.find('my'))
#>>> 6 
print(my_self.find('lo'))
#>>> 3

# <<<------------>>>
my_self="Hello my name is Dilshod"
# index() - Searches the target string for a given substring.
# index() This method is identical to .find(), except that it raises an exception if <sub> is not found rather than returning -1:
print(my_self.index('my'))
#>>> 6

# <<<------------>>>
my_self="Hello my name is Dilshod"
# rfind () - Searches the target string for a given substring starting at the end.
# rfind () - my_self.rfind(<sub>) returns the highest index in my_self where substring <sub> is found:
print(my_self.rfind('i'))
#>>>18

# <<<------------>>>
my_self="Hello my name is Dilshod"
# startwith() - Determines whether the target string starts with a given substring.
# startwith() When you use the Python .startswith() method, my_self.startswith(<suffix>) returns True if my_self starts with the specified <suffix> and False otherwise:
print(my_self.startswith('Hello'))
#>>> True


# Character Classification
# Methods in this group classify a string based on the characters it contains.

# <<<------------>>>
thing='AGBFs123'
# isalnum() - Determines whether the target string consists of alphanumeric characters.
# isalnum() thing.isalnum() returns True if thing is nonempty and all its characters are alphanumeric (either a letter or a number), and False otherwise:
print(thing.isalnum())
#>>> True
thing_2='Hdjsd123$%'
print(thing_2.isalnum())
#>>> False

# <<<------------>>>
thing='AGBFsdhakfb'
# isalpha() -Determines whether the target string consists of alphabetic characters.
# isalpha() thing.isalpha() returns True if thing is nonempty and all its characters are alphabetic, and False otherwise:
print(thing.isalpha())
#>>> True
thing='dgdj123'
print(thing.isalpha())
#>>> False

# <<<------------>>>
# isdigit() -Determines whether the target string consists of digit characters.
# isdigit() You can use the .isdigit() Python method to check if your string is made of only digits. 
# thing.isdigit() returns True if thing is nonempty and all its characters are numeric digits, and False otherwise:
thing='123'
print(thing.isdigit())
#>>> True
thing='advf123'
print(thing.isdigit())
# >>> False


# <<<------------>>>
# isidentifier() - Determines whether the target string is a valid Python identifier.
# thing.isidentifier() returns True if thing is a valid Python identifier according to the language definition, and False otherwise:
thing='hello123'
print(thing.isidentifier())
#>>> True
thing='123hello'
print(thing.isidentifier())
#>>> False


# <<<------------>>>
# islower() - Determines whether the target string’s alphabetic characters are lowercase.
# islower() thing.islower() returns True if thing is nonempty and all the alphabetic characters it contains are lowercase, 
# and False otherwise. Non-alphabetic characters are ignored:
thing='hello34'
print(thing.islower())
#>>> True
thing="Hello34"
print(thing.islower())
# >>> False

# <<<------------>>>
thing='hello34'
# isprintable() -Determines whether the target string consists entirely of printable characters.
# isprintable() returns True if thing is empty or all the alphabetic characters it contains are printable. 
# It returns False if thing contains at least one non-printable character. Non-alphabetic characters are ignored:
print(thing.isprintable())
#>>>True
thing='a\tb'
print('a\tb'.isprintable())
#>>>False


# <<<------------>>>
thing=' \t \n '
# isspace() -Determines whether the target string consists of whitespace characters.
# isspace()  returns True if thing is nonempty and all characters are whitespace characters, and False otherwise.
# The most commonly encountered whitespace characters are space ' ', tab '\t', and newline '\n':
print(thing.isspace())
#>>>True
thing=' a g  '
print(thing.isspace())
#>>>False


# <<<------------>>>
# istitle() -Determines whether the target string is title cased.
# istitle() returns True if my_self is nonempty, the first alphabetic character of each word is uppercase, 
# and all other alphabetic characters in each word are lowercase. It returns False otherwise:
my_self="Hello Dilshod How Are You "
print(my_self.istitle())
#>>>True
my_self="hello Dilshod How are You "
print(my_self.istitle())
#>>>False



# <<<------------>>>
# isupper()- Determines whether the target string’s alphabetic characters are uppercase.
# isupper() my_self.isupper() returns True if my_self is nonempty and all the alphabetic characters it contains are uppercase, and False otherwise. 
# Non-alphabetic characters are ignored:
my_self="HELLO DILSHOD HOW ARE YOU  "
print(my_self.isupper())
#>>>True
my_self="Hello Dilshod How Are You "
print(my_self.isupper())
#>>>False

# String Formatting
# Methods in this group modify or enhance the format of a string.


# <<<------------>>>
# center()-Centers a string in a field.
# center() s.center(<width>) returns a string consisting of s centered in a field of width <width>. By default, padding consists of the ASCII space character:
s='hello'
print(s.center(20))
#>>>'     hello     '
# If the optional <fill> argument is specified, it is used as the padding character:
s='hello'
print(s.center(20,'-'))
#>>>-------hello--------



# <<<------------>>>
# expandtabs(tabsize=8)-Expands tabs in a string.
# expandtabs()  s.expandtabs() replaces each tab character ('\t') with spaces. By default, spaces are filled in assuming a tab stop at every eighth column:
s='a\tb\tc'
print(s.expandtabs())
#>>> a       b       c
#tabsize is an optional keyword parameter specifying alternate tab stop columns:
print(s.expandtabs(4))
#>>> a   b   c


# <<<------------>>>
# ljust -Left-justifies a string in field.
# ljust s.ljust(<width>) returns a string consisting of s left-justified in a field of width <width>. By default, padding consists of the ASCII space character:
s='work'
print(s.ljust(20))
#>>>work
s='work'
print(s.ljust(20,'*'))
#work****************

# <<<------------>>>
# lstrip() -Trims leading characters from a string.
# lstrip()  s.lstrip() returns a copy of s with any whitespace characters removed from the left end:
s='   hello dilshod how are you   '
print(s.lstrip())
#>>>hello dilshod how are you


# <<<------------>>>
# replace()-Replaces occurrences of a substring within a string.
# replace() In Python, to remove a character from a string, you can use the Python string 
# .replace() method. s.replace(<old>, <new>) returns a copy of s with all occurrences of substring <old> replaced by <new>:
s='hello dilshod how are you'
print(s.replace('hello','hi'))
#>>>hi dilshod how are you

# <<<------------>>>
# rjust()-Right-justifies a string in a field.
# rjust()  s.rjust(<width>) returns a string consisting of s right-justified in a field of width <width>. 
# By default, padding consists of the ASCII space character:
s='hello dilshod how are you     '
print(s.rjust(50, '-'))
# --------------------hello dilshod how are you 


# <<<------------>>>
# strip()-Strips characters from the left and right ends of a string.
# strip() As with .lstrip() and .rstrip(), the optional <chars> argument specifies the set of characters to be removed:
s='hello dilshod how are  you '
print(s.strip('hello you'))
# dilshod how ar


# <<<------------>>>
# zfill()- Pads a string on the left with zeros.
# zfill()- s.zfill(<width>) returns a copy of s left-padded with '0' characters to the specified <width>:
s='45'
print(s.zfill(6))
#>>>000045


# Converting Between Strings and Lists    

# Methods in this group convert between a string and some composite data type by either pasting objects together to make a string, or by breaking a string up into pieces.

# These methods operate on or return iterables, the general Python term for a sequential collection of objects. You will explore the inner workings of iterables in much more detail in the upcoming tutorial on definite iteration.

# Many of these methods return either a list or a tuple. These are two similar composite data types that are prototypical examples of iterables in Python. They are covered in the next tutorial, so you’re about to learn about them soon! Until then, simply think of them as sequences of values. A list is enclosed in square brackets ([]), and a tuple is enclosed in parentheses (()).

# With that introduction, let’s take a look at  this last group of string methods.


# <<<------------>>>
# join()-Concatenates strings from an iterable.
# join()-s.join(<iterable>) returns the string that results from concatenating the objects in <iterable> separated by s.
# Some sample code should help clarify. In the following example, the separator s is the string ', ', and <iterable> is a list of string values:
friends=['Ohun','Saidakabr','Toshpulod']
print(':'.join(friends))
#>>>Ohun,Saidakabr,Toshpulod
s='hello'
print(list(s))
#>>>['h', 'e', 'l', 'l', 'o']


# <<<------------>>>
# partition()-Divides a string based on a separator.
# partition()-s.partition(<sep>) splits s at the first occurrence of string <sep>. The return value is a three-part tuple consisting of:
# The portion of s preceding <sep>
# <sep> itself
# The portion of s following <sep>
s='hello$my$name$is$Dilshod'
print(s.partition('$'))
#>>>('hello', '$', 'my$name$is$Dilshod')

# <<<------------>>>
# rsplit()-Splits a string into a list of substrings.
# rsplit()-Without arguments, s.rsplit() splits s into substrings delimited by any sequence of whitespace and returns the substrings as a list:
s='hello my name is dilshod'
print(s.rsplit())
#>>>['hello', 'my', 'name', 'is', 'dilshod']
s='hello:my:name:is:dilshod'
print(s.split(sep=':'))
#>>>['hello', 'my', 'name', 'is', 'dilshod']


# <<<------------>>>
# split()-Splits a string into a list of substrings.
# split()-s.split() behaves exactly like s.rsplit(), except that if <maxsplit> is specified, 
# splits are counted from the left end of s rather than the right end:
s='hello:my:name:is:dilshod'
print(s.split(':',maxsplit=2))
#>>>['hello', 'my', 'name:is:dilshod']






























#Very often in our programmes, we will be dealing with numbers but almost as often,if not more  we will want to deal with text
#For example the user will be giving us some text  and we will be doing some processing on it  as well as we will be waiting some text out to the screen 
#And that is where the next datatype comes in In python  we have got another type called strings that are used to contain text like characters
my_string='hello world'
print(my_string)
# <<<------------>>>
string_with_quotes="Hello   it is me "
another_with_quotes='he said "you are good boy"  !'
multiline =""" Hello world
My name is Dilshod 
"""
print(multiline)
#The + Operator
# <<<------------>>>
a="Hello"
b="Dilshod"
c="How are you "
greeting=a+b+c
print(greeting)
# The * Operator
c='you '
v='me'
d='we'
print(c*4)
# The in Operator
s='hello'
b='hello world how are you '
print('hello ' in b )
print(s in b)
# There is also a not in operator, which does the opposite:
s='hello'
b='hello world how are you '
print('hello '  not in b )
print(s not in b)
# <<<------------>>>
name= 'Jane'
greeting='hello'+name
print(greeting)
# <<<------------>>>
age="25"
print("you are "+age)
age_as_str=str(age)
print("You are "+ age_as_str)
# <<<------------>>>
age=25
print(f"You are {age}")
# <<<------------>>>
name="Dilshod"
greeting=f"How are you ,{name}"
print(greeting)
# <<<------------>>>
name="Dilshod"
final_greeting="How are you ,{}"
dilshod_greeting=final_greeting.format(name)
print(dilshod_greeting)
# <<<------------>>>
name="Javlon"
dilshod_greeting=final_greeting.format(name)
print(dilshod_greeting)
# <<<------------>>>
name="Dilshod"
final_greeting="How are you ,{name}"
dilshod_greeting=final_greeting.format(name="Dilshod")
print(dilshod_greeting)
# <<<------------>>>
name=input("Enter your name :")
final_greeting="How are you ,{name}"
dilshod_greeting=final_greeting.format(name=name)
print(dilshod_greeting)
# Getting user input in Pyhton 
first_name="Tom"
friend_name=input("Enter your friend name : ")
print(f"Hello {first_name}.My friend name is {friend_name}")
# <<<------------>>>
age=input('Enter your age :')
age_num=int(age)
print(f"You have lived for {age_num*12} months")
# <<<------------>>>
age=int(input('Enter your age :'))
print(f"You have lived for {age*12} months")
# <<<------------>>>
age=int(input('Enter your age :'))
months=age*12
print(f"You have lived for {months} months")
# Built-in String Functions
# chr---->>> Converts an integer to charc

































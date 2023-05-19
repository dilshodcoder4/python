# # 1. Write a Python program to find those numbers 
# # which are divisible by 7 and multiples of 5, 
# # between 1500 and 2700 (both included)
# list_for_numbers=[]
# for x in range(1500,2700):
#     if x%7==0 and x%5==0:
#         list_for_numbers.append(str(x))
# print(','.join(list_for_numbers))        
  
# >>>1505,1540,1575,1610,1645,1680,1715,1750,1785,
# 1820,1855,1890,1925,1960,1995,2030,2065,2100,2135,
# 2170,2205,2240,2275,2310,2345,2380,2415,
# 2450,2485,2520,2555,2590,2625,2660,2695   

# # 2. Write a Python program to convert temperatures to 
# # and from Celsius and Fahrenheit

# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]

# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")


# #>>> Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : 60f
# #>>> The temperature in Celsius is 16 degrees.


# # 3. Write a Python program to guess a number between 1 and 9.
# # Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
# # on successful guess, user will get a "Well guessed!" message, and the program will exit.
# import random
# numbers=[1,2,3,4,5,6,7]
# random_number=random.choice(numbers)
# user_guess_number=int(input("Imput the number"))
# while True:
#     if user_guess_number==random_number:
#         print("Correct")
#         break
#     else:
#         print("Uncorrect Please Try again : Yes/No :")
#         user_choise=(input(":"))
#         if user_choise=="Yes":
#             user_guess_number=int(input("Imput the number"))
#         else:
#             break

# # 4. Write a Python program to construct the following pattern, using a nested for loop.


# def checker(n):
#     for i in range(n):
#         for j in range(i):
#             print ('* ', end="")
#         print('')        

#     for i in range(n,0,-1):
#         for j in range(i):
#             print('* ', end="")
#         print('')
        
# n=int(input("Input the number :")) 
# while True:        
#     checker(n)
#     print("Yes/No")
#     user_input=input(":")
#     if user_input=='Yes':
#         n=int(input("Input the number :"))
#         continue
#     else:
#         break   
            
# # 5. Write a Python program that accepts a word from the user and reverses it.         
# word=input("Input the word to reverse :")   
# for char in range(len(word) - 1, -1, -1):
#   print(word[char], end="")
# print("\n")          
        
# # 6. Write a Python program to count the number of even and odd numbers in a series of numbers 
# numbers_list=[1,2,3,4,5,6,4,8,9,10,11,12,13,14,15]   
# even_numbers=[]
# odd_numbers=[]
# for x in numbers_list:
#     if x%2==0:
#         even_numbers.append(x)
#     else:
#         odd_numbers.append(x)
        
# print(f"Odd numbers are {odd_numbers}")
# print(f"Even numbers are {even_numbers}")              
    
    
# # 7. Write a Python program that prints each item and its corresponding type from the following list.
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# for x in datalist:
#     print(f"The type {x} is  {type(x)}")    
# # >>>    
# # The type 1452 is  <class 'int'>
# # The type 11.23 is  <class 'float'>
# # The type (1+2j) is  <class 'complex'>
# # The type True is  <class 'bool'>
# # The type w3resource is  <class 'str'>
# # The type (0, -1) is  <class 'tuple'>
# # The type [5, 12] is  <class 'list'>
# # The type {'class': 'V', 'section': 'A'} is  <class 'dict'>    

# # 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# for x in range(0,6):
#     if x==3:
#         x=""
#         continue 
#     else:
#         print(x)   
        
# # 9. Write a Python program to get the Fibonacci series between 0 and 50.
# x,y=0,1

# while y<50:
#     print(y)
#     x,y=y,x+y        
        
# # >>>       
# # 1
# # 1
# # 2
# # 3
# # 5
# # 8
# # 13
# # 21
# # 34

# # 10. Write a Python program that iterates the integers from 1 to 50. 
# # For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
# # For numbers that are multiples of three and five, print "FizzBuzz".

# number=int(input("Enter the number : "))
# for x in range(number):
    
#     if x%3==0 and x%5==0:
#         print("FizzBuzz")
#     elif x%5==0:
#         print("Buzz")    
#     elif x%3==0:
#         print("Fizz")
#     else:
#         print(x)
    
# # Enter the number : 20
# # FizzBuzz
# # 1
# # 2
# # Fizz
# # 4
# # Buzz
# # Fizz
# # 7
# # 8
# # Fizz
# # Buzz
# # 11
# # Fizz
# # 13
# # 14
# # FizzBuzz
# # 16
# # 17
# # Fizz
# # 19

# # 11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# # The element value in the i-th row and j-th column of the array should be i*j.

# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col

# print(multi_list)

# #  12. Write a Python program that accepts a 
# # sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
# words=[]
# while True:
#     letter=input()
#     if letter:
#         words.append(letter.upper())
#     else:
#         break;
    
# for letter in words:
#     print(letter)        
# # >>>
# # dilshdo
# # qalesan

# # DILSHDO
# # QALESAN
# 13. Write a Python program that accepts a sequence of comma 
# separated 4 digit binary numbers as its input. 
# The program will print the numbers that are divisible by 5 in a comma separated 
binary=[]
binary2=[]

number=int(input("=>"))
for x in range(0,number):
    x=int(input(">>>> "))
    binary.append(x)
        
for c in binary:
    if c%5==0:
        binary2.append(c) 
    
        
print(binary2)
       
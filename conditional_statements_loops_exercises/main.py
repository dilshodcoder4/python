# # 1. Write a Python program to find those numbers 
# # which are divisible by 7 and multiples of 5, 
# # between 1500 and 2700 (both included)
# list_for_numbers=[]
# for x in range(1500,2700):
#     if x%7==0 and x%5==0:
#         list_for_numbers.append(str(x))
# print(','.join(list_for_numbers))        
  
# # >>>1505,1540,1575,1610,1645,1680,1715,1750,1785,
# # 1820,1855,1890,1925,1960,1995,2030,2065,2100,2135,
# # 2170,2205,2240,2275,2310,2345,2380,2415,
# # 2450,2485,2520,2555,2590,2625,2660,2695   

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


# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
# on successful guess, user will get a "Well guessed!" message, and the program will exit.
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

# 4. Write a Python program to construct the following pattern, using a nested for loop.


def checker(n):
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')        

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')
        
n=int(input("Input the number :")) 
while True:        
    checker(n)
    print("Yes/No")
    user_input=input(":")
    if user_input=='Yes':
        n=int(input("Input the number :"))
        continue
    else:
        break   
            
            
        
    
# 1. Write a Python program to find those numbers 
# which are divisible by 7 and multiples of 5, 
# between 1500 and 2700 (both included)
list_for_numbers=[]
for x in range(1500,2700):
    if x%7==0 and x%5==0:
        list_for_numbers.append(str(x))
print(','.join(list_for_numbers))        
  
# >>>1505,1540,1575,1610,1645,1680,1715,1750,1785,
# 1820,1855,1890,1925,1960,1995,2030,2065,2100,2135,
# 2170,2205,2240,2275,2310,2345,2380,2415,
# 2450,2485,2520,2555,2590,2625,2660,2695   














import random
numbers=[1,2,3,4,5,6,7]
random_number=random.choice(numbers)
user_guess_number=int(input("Imput the number"))
while True:
    if user_guess_number==random_number:
        print("Correct")
        break
    else:
        print("Uncorrect Please Try again : Yes/No :")
        user_choise=(input(":"))
        if user_choise=="Yes":
            user_guess_number=int(input("Imput the number"))
        else:
            break 
        


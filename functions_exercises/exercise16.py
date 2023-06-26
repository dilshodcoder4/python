# 16. Write a Python function to create and print a list where the 
# values are the squares of numbers between 1 and 30 (both included)
def square_of_numbers(number):
    sqrd=[]
    for x in range(1,number):
        sqrd.append(x**2)      
    print(sqrd)    
square_of_numbers(10)

# >>>[1, 4, 9, 16, 25, 36, 49, 64, 81]
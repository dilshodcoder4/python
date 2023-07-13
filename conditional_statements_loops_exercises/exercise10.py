# 10. Write a Python program that iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
# For numbers that are multiples of three and five, print "FizzBuzz".

number=int(input("Enter the number : "))
for x in range(number):
    
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%5==0:
        print("Buzz")    
    elif x%3==0:
        print("Fizz")
    else:
        print(x)
    
# Enter the number : 20
# FizzBuzz
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
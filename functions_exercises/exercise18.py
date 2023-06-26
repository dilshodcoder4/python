# 18. Write a Python program to execute a string containing Python code.

greeting='print("My name is Dilshod")'
calculation="""
def sum_of_two_numbers(s,v):
    print(s+v)
sum_of_two_numbers(6,2)
"""

exec(greeting)
exec(calculation)

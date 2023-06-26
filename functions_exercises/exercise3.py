# 3. Write a Python function to multiply all the numbers in a list
def multiply(numbers):
    total=1
    for x in numbers:
        total=total*x
    return total 
print(multiply((1,2,3,4)))    
# >>> 24

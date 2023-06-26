# 1. Write a Python function to find the maximum of three numbers.

def max_of_two_number(a,b):
    if a>b:
        return a
    else:
        return b
    
def max_of_three_number(b,a,c):
    return max_of_two_number(a,max_of_two_number(a,b))
     
print(max_of_three_number(9,4,5))   

# >>> 9
    
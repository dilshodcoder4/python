# Write a Python function to check whether a number falls within a given range
def check_number(number):
    if number in range(2,90):
        print(f"There is {number} between to 2 and 90")
    else:
        print("There is not here")    
        
check_number(4)        
# >>> There is 4 between to 2 and 90
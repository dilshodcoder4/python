        # 6. Write a Python program to count the number of even and odd numbers in a series of numbers 
numbers_list=[1,2,3,4,5,6,4,8,9,10,11,12,13,14,15]   
even_numbers=[]
odd_numbers=[]
for x in numbers_list:
    if x%2==0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)
        
print(f"Odd numbers are {odd_numbers}")
print(f"Even numbers are {even_numbers}")    
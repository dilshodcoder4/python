# 14. Write a Python program that accepts a string and calculates the number of digits and letters.
numbers=['1','2','3','4','5','6','7','8','9','0']
element=input("Enter the string :")
digits=[]
letters=[]
for digit in element:
    if digit in numbers:
        digits.append(digit)       
    else:
        letters.append(digit)    
print(f"There are {len(digits)} digits in the string")
print(f"There are {len(letters)} letters in the string")

# 2-second way 

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
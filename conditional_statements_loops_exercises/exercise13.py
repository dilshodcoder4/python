# 13. Write a Python program that accepts a sequence of comma 
# separated 4 digit binary numbers as its input. 
# The program will print the numbers that are divisible by 5 in a comma separated 
binary=[]
binary2=[]

number=int(input("How many elements do you wanna store: "))
for x in range(0,number):
    x=int(input("_"))
    binary.append(x)
        
for c in binary:
    if c%5==0:
        binary2.append(c) 
    
        
print(binary2)
       
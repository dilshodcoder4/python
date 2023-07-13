# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
# The numbers obtained should be printed in a comma-separated sequence.

empty_list=[]
for c in range(101,401):
    c=str(c)
    if (int(c[0])%2==0) and (int(c[1])%2==0) and (int(c[2])%2==0):
        empty_list.append(c)
       
print("-".join(empty_list)) 
        
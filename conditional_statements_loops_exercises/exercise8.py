# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for x in range(0,6):
    if x==3:
        x=""
        continue 
    else:
        print(x)   
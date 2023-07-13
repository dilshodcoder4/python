# 4. Write a Python program to construct the following pattern, using a nested for loop.


def checker(n):
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')        

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')
        
n=int(input("Input the number :")) 
while True:        
    checker(n)
    print("Yes/No")
    user_input=input(":")
    if user_input=='Yes':
        n=int(input("Input the number :"))
        continue
    else:
        break   
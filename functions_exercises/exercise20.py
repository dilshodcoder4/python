# 20. Write a Python program to detect the number of local variables declared in a function.
def abc():
    v=1
    y=2
    str1="hello my name is Dilshod"
    print("Python is very good programming langueage")
    
print(abc.__code__.co_nlocals)    
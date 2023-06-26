
# 19. Write a Python program to access a function inside a function.
def new(number):
    def add(num):
        nonlocal number
        number+=1
        return num+number
    return add
my_func=new(8)
print(my_func(8))

#Integers and Floating-Point Numbers
#There are two main types of numbers in python  and that is integers or whole numbers and floating point numbers or numbers with decimal place  
# For example :
age =21 #integer
PI=3.14159 #float
# An integer is an whole number with no decimal places .For exapla  1 is an integer  but
# 1.0 isn't ,The name for the integer data type is int ,which you can see with type()
print(type(2))
# we can aslo convert a string containing an integer to a nuber  using int()
int("25")
# >> 25 
#Like integers, floats can be created from floating-point literals or by converting a string to a float with float():
float("1.25")
# >>1.25
#Mathematics works just as normally , so we might have  a variable named math operation
maths_operation=20+2*9/2-5
# as long as we can verify this via printing it 
print(maths_operation)
# one more information  which is important part of mathematics in python  the reason is that  whenever you use division, you always get float 
# example 
float_division=31/5
print(float_division)
# if you want to get rid of the  floating point or the decimal place  so you can do integer division
integer_division=21//4
print(integer_division)

#Math Operators in Python 
# Exponent ==== (**)  2**3=8
a=3
b=4
x=a**b
print(x)
# Modules / reminder =====(%) 22%8=6
a=10
b=3
x=a%b
print(x)
# Integer devision /floored quotiet ====(//) 12//5=2
a=9
b=2
x=a//b
print(x)
#Devision ======(/) 20/5=4
a=16
b=8
x=a/b
print(x)
#Multiplication======(*) 20*5=100
a=16
b=8
x=a*b
print(x)
#Subtraction ======(-) 20-5=16
a=16
b=8
x=a-b
print(x)
#Addition ======(+) 20+5=25
a=16
b=8
x=a+b
print(x)





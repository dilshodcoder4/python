# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
import pprint
def TreeNum(a,b,c):
    list1= [ [ ['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return list1

num1=3
num2=4
row=5
pprint.pprint(TreeNum(num1,num2,row))
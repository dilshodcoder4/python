# 1. Write a Python program to sum all the items in a list
# 1-way
def sum_checker(items):
    sum_of_all=0
    for x in items:
        sum_of_all+=x
        
    print(sum_of_all)    
    
list=[1,2,3,4,5,6,7]    
sum_checker(list)
#>>> 28


# 2-way you can easly use sum() to calculate sum of all items
list=[1,2,3,4,5,6,7]
print(sum(list))   
#>>> 28













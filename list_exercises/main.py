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

# 2. Write a Python program to multiply all the items in a list.
def multiply(items):
    multiply_of_all=1
    for x in items:
        multiply_of_all*=x
        
    print(multiply_of_all)
list=[1,2,3,4,5,6,7]
multiply(list)        
#>>>5040

# 3. Write a Python program to get the largest number from a list. 
# 1-way
list=[1,2,3,4,5,6,7]
max_score=1
for score in list:
    if score>=max_score:
        max_score=score
    
print(max_score)     
#>>>7
#2-way
print(max(list))
#>>>7











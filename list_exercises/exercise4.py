# 4. Write a Python program to get the smallest number from a list. 
list=[1,2,3,4,5,6,7]
min_element=1
for score in list:
    if min_element>=score:
        min_element=score
        
print(min_element)
#>>> 1
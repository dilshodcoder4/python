# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def remove_the_same_emlements(n):
    new_list=[]
    for x in n:
        if x not in  new_list:
            new_list.append(x)
        else:
            continue   
    print(new_list)     
        
        
remove_the_same_emlements([1,2,3,4,5,6,7,8,9,9,8,1])      
#>>>[1, 2, 3, 4, 5, 6, 7, 8, 9]
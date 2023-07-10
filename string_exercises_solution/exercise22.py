# 22.Write a Python program to sort a string lexicographically.
def sorter(n):
    empty_list=[]
    for x in n:
        empty_list+=x
        empty_list.sort()
    print(empty_list)  
    
sorter("hello")    
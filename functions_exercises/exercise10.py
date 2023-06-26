
# 10. Write a Python program to print the even numbers from a given list. 
def even_sorter(n):
    even_numbers=[]
    for number in n:
        if number%2==0:
            even_numbers.append(number)      
        else:
            continue
    print(even_numbers)    
c=[1,2,3,4,5,6,7,8]        
even_sorter(c)              
#>>>[2, 4, 6, 8]

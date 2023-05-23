# # 1. Write a Python function to find the maximum of three numbers.

# def max_of_two_number(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# def max_of_three_number(b,a,c):
#     return max_of_two_number(a,max_of_two_number(a,b))
     
# print(max_of_three_number(9,4,5))   

# # >>> 9
    
# # 2. Write a Python function to sum all the numbers in a list
# def sum(numbers):
#     total=0
#     for x in numbers:
#         total+=x
#     return total
# print(sum((1,2,3,4,5)))
# # >>> 15

# # 3. Write a Python function to multiply all the numbers in a list
# def multiply(numbers):
#     total=1
#     for x in numbers:
#         total=total*x
#     return total 
# print(multiply((1,2,3,4)))    
# # >>> 24



# # 4. Write a Python program to reverse a string.
# def revverse(string):
#     return string[::-1]

# print(revverse('hello'))

# # >>> olleh

# # 5. Write a Python function to calculate the factorial of a number (a non-negative integer).
# # The function accepts the number as an argument.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Enter a  number to compute the factiorial : "))
# print(factorial(n))      


# # Write a Python function to check whether a number falls within a given range
# def check_number(number):
#     if number in range(2,90):
#         print(f"There is {number} between to 2 and 90")
#     else:
#         print("There is not here")    
        
# check_number(4)        
# # >>> There is 4 between to 2 and 90

# # 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# def upper_lower_counter(string):
#     lower=0
#     upper=0
#     for x in string:
#         if x==x.upper():
#             upper+=1
#         else:
#             lower+=1
#     print(f"There is {lower} lower letter(s) in the word") 
#     print(f"There is {upper} upper letter(s) in the word")           
                
# upper_lower_counter("hEllo")

# # >>>There is 4 lower letter(s) in the word
# # >>>There is 1 upper letter(s) in the word

# # 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# def remove_the_same_emlements(n):
#     new_list=[]
#     for x in n:
#         if x not in  new_list:
#             new_list.append(x)
#         else:
#             continue   
#     print(new_list)     
        
        
# remove_the_same_emlements([1,2,3,4,5,6,7,8,9,9,8,1])      
# #>>>[1, 2, 3, 4, 5, 6, 7, 8, 9]

# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# def check_prime(number):
#     prime_number=True


#     for i in range(2,number):
#         if number%i==0:
#             prime_number=False
#     if prime_number:
#         print(f"{number} is prime number")
#     else:
#         print(f"{number} is not prime number")             

# user=int(input("Imput number: "))
# check_prime(user)

# # 10. Write a Python program to print the even numbers from a given list. 
# def even_sorter(n):
#     even_numbers=[]
#     for number in n:
#         if number%2==0:
#             even_numbers.append(number)      
#         else:
#             continue
#     print(even_numbers)    
# c=[1,2,3,4,5,6,7,8]        
# even_sorter(c)              
# #>>>[2, 4, 6, 8]

# # 11. Write a Python function to check whether a number is "Perfect" or not. 
# def perfect_number(n):
#     empty_list=[]
#     for number in range(1,n):
#         if n%number==0:
#             empty_list.append(number)
#         else:
#             continue
#     if sum(empty_list)==n:
#         print(f"{n} is perfect number")
#     else:
#         print(f"{n} is not perfect number")            
        
# perfect_number(496)
# #>>>496 is perfect number

# # 12. Write a Python function that checks whether a passed string is a palindrome or not.
# def palindrome(n):
#     if n==n[::-1]:
#         print("this is palindrome")
#     else:
#         print("this is not palindrome")    
        
# palindrome("madam")        
# #>>>this is palindrome

# # 13. Write a Python function that prints out the first n rows of Pascal's triangle
# def pascal_triangle(n):
#     triangle = [[1]]
#     for i in range(1, n):
#         row = [1]
#         for j in range(1, i):
#             row.append(triangle[i-1][j-1] + triangle[i-1][j])
#         row.append(1)
#         triangle.append(row)
#     for row in triangle:
#         print(row)

# pascal_triangle(5)
# #>>>
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]

# # 14. Write a Python function to check whether a string is a pangram or not
# def is_pangram(sentence):
    
#     alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
 
#     letters = set(filter(lambda x: x.isalpha(), sentence.lower()))
    
#     return letters == alphabet       
# print(is_pangram("Hello my name is Dilshod"))
# # >>>False

# # 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words
# # in a hyphen-separated sequence after sorting them alphabetically.

# def SorterWithLetter(string):
#     x=string.split()
#     x.sort()
#     sorted_string=" "
#     for sorted in x:
#         sorted_string+=sorted
#         sorted_string+=" "
#     print(sorted_string)    
       
# SorterWithLetter("hello my name is dilshod ")      
# # >>>dilshod hello is my name  



# # 16. Write a Python function to create and print a list where the 
# # values are the squares of numbers between 1 and 30 (both included)
# def square_of_numbers(number):
#     sqrd=[]
#     for x in range(1,number):
#         sqrd.append(x**2)      
#     print(sqrd)    
# square_of_numbers(10)

# # >>>[1, 4, 9, 16, 25, 36, 49, 64, 81]

# # 17. Write a Python program to create a chain of 
# # function decorators (bold, italic, underline etc.).
# def make_bold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped

# def make_italic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped

# def make_underline(fn):
#     def wrapped():
#         return "<u>" + fn() + "</u>"
#     return wrapped
# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return "hello dilshod"
# print(hello()) ## returns "<b><i><u>hello dilshod</u></i></b>"  


# # 18. Write a Python program to execute a string containing Python code.

# greeting='print("My name is Dilshod")'
# calculation="""
# def sum_of_two_numbers(s,v):
#     print(s+v)
# sum_of_two_numbers(6,2)
# """

# exec(greeting)
# exec(calculation)


# # 19. Write a Python program to access a function inside a function.
# def new(number):
#     def add(num):
#         nonlocal number
#         number+=1
#         return num+number
#     return add
# my_func=new(8)
# print(my_func(8))
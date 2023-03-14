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


            
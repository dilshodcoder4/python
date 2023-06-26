# 12. Write a Python function that checks whether a passed string is a palindrome or not.
def palindrome(n):
    if n==n[::-1]:
        print("this is palindrome")
    else:
        print("this is not palindrome")    
        
palindrome("madam")        
#>>>this is palindrome
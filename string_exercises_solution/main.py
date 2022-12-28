
# 1. Write a Python program to calculate the length of a string.
# def calculate_length_of_string(strr):
#     print(len(strr))
# calculate_length_of_string('hello')    


# # 2. Write a Python program to count the number of characters (character frequency) in a string.
# word=input("Enter word :")
# x=len(word)
# for n in range(x):
#     print(f'{word[n]} >>> {word.count(word[n])}')
   

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string
# def swapchar(string):
#     if len(string)>2:
#         print(f'{len(string)[0:2]}{len(string)[-2]}{len(string)[-1]}')
#     else:
#         return ''

# swapchar('hello')

#4. Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', except the first char itself
def someword(ty):
    x=len(ty)
    for n in range(x):
        print(f"{ty[n]}")
        if ty[n]==ty[n]:
            return ty[1] = '$'
        

     
someword('hello')
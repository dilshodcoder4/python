# # 18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
def take_three_elemnts(str):
    if len(str)<3:
        return str
    else:
        print(str[:3])    

take_three_elemnts("hello")
#>>>hel

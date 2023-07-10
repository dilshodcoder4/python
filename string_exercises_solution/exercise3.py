# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string
def swapcharr(string):
    if len(string)>2:
        print(f'{string[:2]}{string[-2:]}')
    elif len(string)==2 :
        print(string*2)       
    else:
        return ''

swapcharr('he')
swapcharr('hello')
swapcharr('h')

#Expected Result
#>>>hehe
#>>>helo
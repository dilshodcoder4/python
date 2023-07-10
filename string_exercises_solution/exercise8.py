# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one
def return_lengh_of_value(a):
    return len(a)

word=input('Enter the word :')
x=word.split()
b=len(x)
x.sort(key=return_lengh_of_value)
print(x)
print(x[b-1])

#>>>['is', 'boy', 'good', 'dilshod']
#>>>dilshod

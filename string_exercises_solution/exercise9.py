
# 9. Write a Python program to remove the nth index character from a nonempty string. 
word=input('Enter the word :')
n=int(input("Which index character that you want to change :"))
print(word.replace(word[n],''))

# >>> Enter the word :dilshod is bad guy
# >>> Which index character that you want to change :2
# >>> dishod is bad guy
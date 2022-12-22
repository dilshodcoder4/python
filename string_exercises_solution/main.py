# 2. Write a Python program to count the number of characters (character frequency) in a string.
word=input("Enter word :")
x=len(word)
for n in range(x):
    print(f'{word[n]} >>> {word.count(word[n])}')
   


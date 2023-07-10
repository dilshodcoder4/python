
# 2. Write a Python program to count the number of characters (character frequency) in a string.
word=input("Enter word :")
x=len(word)
for n in range(x):
    print(f'{word[n]} >>> {word.count(word[n])}')

# Expected Result
# >>>  e >>> 3
# >>>  x >>> 1
# >>>  e >>> 3
# >>>  r >>> 1
# >>>  c >>> 1
# >>>  i >>> 1
# >>>  s >>> 2
# >>>  e >>> 3
# >>>  s >>> 2    
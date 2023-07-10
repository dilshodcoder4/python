# 5. Write a Python program to get a single string from two given strings,
#  separated by a space and swap the first two characters of each string.
word1=input('Enter first word:')
word2=input('Enter second word:')
print(f'{word1.replace(word1[:2],word2[:2])} {word2.replace(word2[:2],word1[:2])}')

# Expected Result
#>>> Enter first word:dello
#>>> Enter second word:dilshod
#>>> dillo delshod
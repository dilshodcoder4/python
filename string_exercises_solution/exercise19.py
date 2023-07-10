# # 19. Write a Python program to get the last part of a string before a specified character.
word=input("Imput word:")
word2=word.split()
word3=word2[:-1]
empty_string=""
for x in word3:
    empty_string=empty_string+x

print(empty_string)
#>>>Imput word:hewll kjfdgksd fdjgkg
#>>>hewllkjfdgksd
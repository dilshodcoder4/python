# # 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
words=input("Imput the string : ")
empty_upper=0
empty_lower=0
x=len(words)
for word in words[:4]:
    if word==word.upper():
        empty_upper+=1
if empty_upper>=2:
    print(words.upper())        
    
else:
    print(words.lower())   
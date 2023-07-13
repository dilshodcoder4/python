#  12. Write a Python program that accepts a 
# sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
words=[]
while True:
    letter=input()
    if letter:
        words.append(letter.upper())
    else:
        break;
    
for letter in words:
    print(letter)        
# >>>
# dilshdo
# qalesan

# DILSHDO
# QALESAN
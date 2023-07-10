# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
word=input("Imput the word :")
if len(word)<2:
    print("Please try again")
else:    
    print(word[-2:]*4)

#>>> Imput the word :dilshod
#>>> odododod
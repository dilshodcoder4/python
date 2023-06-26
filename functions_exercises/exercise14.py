
# 14. Write a Python function to check whether a string is a pangram or not
def is_pangram(sentence):
    
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
 
    letters = set(filter(lambda x: x.isalpha(), sentence.lower()))
    
    return letters == alphabet       
print(is_pangram("Hello my name is Dilshod"))
# >>>False
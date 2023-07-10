# 11. Write a Python program to remove characters that have odd index values in a given string.
def odd_element_change(word):
    excepted_word = ""
    for x in range(len(word)):
        if x %2 == 0:
            excepted_word=excepted_word + word[x]
    return excepted_word

WordToChange=input("Enter the word :")
print(odd_element_change(WordToChange))      

#>>> Enter the word :dilshodbek
#>>> dlhde
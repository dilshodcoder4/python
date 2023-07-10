# # 20. Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_string(wrd):
    if len(wrd)%4==0:
        print(wrd[::-1])
    else:
        print(wrd)

word=input("Imput the word : ")
reverse_string(word)            

#>>>Imput the word : hellodiy
#>>>yidolleh
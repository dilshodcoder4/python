# 12. Write a Python program to count the occurrences of each word in a given sentence
def count_words(str):
    counts=dict()
    words=str.split()


    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts


wordi=input("Enter the word :")
print(count_words(wordi))


#>>> Enter the word :hello how are you 
#>>> {'hello': 1, 'how': 2, 'are': 1, 'you': 3}
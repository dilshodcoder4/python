#14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically)
itmes = input("Input  words :")
words = [word for word in itmes.split(",")]
print(",".join(sorted(list(set(words)))))

# >>> Input  words :hello,is,dilshdo
# >>> dilshdo,hello,is
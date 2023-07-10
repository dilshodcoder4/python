# 15. Write a Python function to create an HTML string with tags around the word(s)
print("""Choose Tag :
1) <i> </i>
2) <b> </b>""")
choise=int(input(""))
word=input("Imput word :")

if choise==1:
    print(f'<i>{word}</i>')
else:
    print(f'<b>{word}</b>')

#>>>   Choose Tag :
 #>>>1) <i> </i>
 #>>>2) <b> </b>
 #>>>1
 #>>>Imput word :hello how are you
 #>>><i>hello how are you</i>
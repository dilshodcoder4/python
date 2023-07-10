# # 16. Write a Python function to insert a string in the middle of a string
print("""Choose Tag :
1)[[]]
2){{}}
3)<<>> """)
choise=int(input("==> :"))
word=input("Imput word :")
if choise==1:
    print(f"[[{word}]]")
elif choise==2:
    print("{{"+f"{word}"+"}}")
else:
    print(f"<<{word}>>")

#>>>Choose Tag :
#>>> 1)[[]]
#>>>2){{}}
#>>>3)<<>> 
#>>>==> :3
#>>>Imput word :hello world
#>>> <<hello world>>
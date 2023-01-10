# 1
friend="Dilshod"
user_name=input("Enter your name ")

if user_name==friend:
    print("Hello,friend") 
    print("This has been working")

print("This runs away ")    

# 2
friend="Dilshod"
user_name=input("Enter your name ")

if user_name==friend:
    print("Hello,friend")
else:
    print("He is not friend")

# 3
print(bool(5))
# True

if 5:
    print('Runs')
# Runs

friends=['Dilshdo','Omadbek','Asal']
family=['Farida','Jahongir','Hojimurod']

user_name=input("Enter your name ")

if user_name in friends:
    print(f"hello{user_name}")
if user_name in family:
    print(f'Hello,{user_name}')    
else:
    print('I do not know you. ')    

#4 create two boolean objects

x = False
y = True
#The validation will be True only if all the expressions generate a value True
if x and y:
    print('Both x and y are True')
else:
    print('x is False or y is False or both x and y are False')

#5 #create a integer
a = 120
print(a)

#if a is greater than 500, a is multiplied by 7, otherwise a is divided by 7
result = a * 7 if a > 500 else a / 7
print(result)    












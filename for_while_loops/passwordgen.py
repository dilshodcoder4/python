import random
letters=[ 'A','B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q,', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k1', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','^','(',')',"*",'+']

print('Welcome to the Dilshod password Generator !')
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like in your password?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))


# 1 -way
password=""
for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password+=random_char
    
for symbol in range(1,nr_symbols+1):
    random_symbol=random.choice(symbols)
    password+=random_symbol    
    
for number in range(1,nr_numbers+1):
    random_number=random.choice(numbers)
    password+=random_number   
    
print(password)    



#2-way
password_list=[]
for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password_list+=random_char
    
for symbol in range(1,nr_symbols+1):
    random_symbol=random.choice(symbols)
    password_list+=random_symbol    
    
for number in range(1,nr_numbers+1):
    random_number=random.choice(numbers)
    password_list+=random_number   
    
print(password_list)    
random.shuffle(password_list)
print(password_list)


password=""
for char in password_list:
    password+=char
    
print(f"Your password is created {password}")    
    
    
    
    

    
# #1
# def greet():
#     name=input("Enter your name :")
#     print('Hello',name)

# greet()

# #2
# car={
#     "make":"Ford",
#     "model":"Fiesta",
#     "mileage":2300,
#     "fuel_consumed":456
# }

# mpg=car["mileage"]/car["fuel_consumed"]
# name=f"{car['make']} {car['model']}"
# print(f"{name} does {mpg} miles per gallon")

# # 3
# def calculate_mpg():
#     car={
#         "make":"Ford",
#         "model":"Fiesta",
#         "mileage":2300,
#         "fuel_consumed":456
#     }

#     mpg=car["mileage"]/car["fuel_consumed"]
#     name=f"{car['make']} {car['model']}"
#     print(f"{name} does {mpg} miles per gallon")

# calculate_mpg()    

# # 4
# def calculate_mpg(car_to_calculate):
#     mpg=car_to_calculate["mileage"]/car_to_calculate["fuel_consumed"]
#     name=f"{car_to_calculate['make']} {car_to_calculate['model']}"
#     print(f"{name} does {mpg} miles per gallon")


# calculate_mpg({
#         "make":"Ford",
#         "model":"Fiesta",
#         "mileage":2300,
#         "fuel_consumed":456
#     })
# # 5
# cars=[{"make":"Ford","model":"Fiesta","mileage":2300, "fuel_consumed":456},
#      {"make":"Bugatti","model":"Chevrolet","mileage":200, "fuel_consumed":120},
#      {"make":"Ferrari","model":"Daewoo","mileage":800, "fuel_consumed":200},
#      {"make":"Nexia","model":"Chevrolet_2","mileage":1200, "fuel_consumed":750}]

# def calculate_mpg(car,intro):
#     print(intro)
#     mpg=car["mileage"]/car["fuel_consumed"]
#     name=f"{car['make']} {car['model']}"
#     print(f"{name} does {mpg} miles per gallon")    



# for car in cars:
#     calculate_mpg(car,"New car")   

# # 6
# cars=[{"make":"Ford","model":"Fiesta","mileage":2300, "fuel_consumed":456},
#      {"make":"Bugatti","model":"Chevrolet","mileage":200, "fuel_consumed":120},
#      {"make":"Ferrari","model":"Daewoo","mileage":800, "fuel_consumed":200},
#      {"make":"Nexia","model":"Chevrolet_2","mileage":1200, "fuel_consumed":750}]

# def calculate_mpg(car):
#     mpg=car["mileage"]/car["fuel_consumed"]
#     return mpg

# def car_name(car):
#     name=f"{car['make']} {car['model']}"
#     return name

# def car_info(car):
#     name=car_name(car)
#     mpg=calculate_mpg(car)
#     print(f"{name} does {mpg} miles per gallon")    



# for car in cars:
#     mpg=car_info(car) 


# # 7
# def devide(x,y):
#     if y==0:
#         return "You tried to divide by zero"    
#     else:    
#         return x/y

# print(devide(70,5))


# # Default parameter values
# # 8
# def add(x,y):
#     total=x+y
#     return total 


# print(add(3,5))    

# # 9
# def add(x,y=4):
#     total=x+y
#     return total 


# print(add(3))    


# # 10
# def add(x,y):
#     total=x+y
#     return total 


# print(add(x=5,y=6))  

# # 11
# default_y=3


# def add(x,y=default_y):
#     total=x+y
#     print(total)


# add(2)



# # Functions with more than 1 input
# # Positional argument 

# def greet_with(name,location):
#     print(f'hello{name}')
#     print(f"What is your city"{location})


# greet_with('Dilshod','Tasheknt')



# #Keyword argument 

# greet_with(name='Dilshod',location='Tasheknt ')

# #Lambda Functions 
# #12
# devide=lambda x,y:x/y

# print(devide(15,3))

# #13
# print((lambda x,y:x/y)(15,3))

# #14
# def average(sequence):
#     return sum(sequence)/len(sequence)


# students=[
#     {'name':'Rolf','grades':(50,25,30,60,90)},
#     {'name':'Sanjar','grades':(40,28,42,63,82)},
#     {'name':'Asal','grades':(25,41,78,55,75)},
#     {'name':'Gani','grades':(35,47,12,50,35)},
# ]

# for student in students:
#     print(average(student["grades"]))

# #15
# average =lambda sequence: sum(sequence)/len(sequence)


# students=[
#     {'name':'Rolf','grades':(50,25,30,60,90)},
#     {'name':'Sanjar','grades':(40,28,42,63,82)},
#     {'name':'Asal','grades':(25,41,78,55,75)},
#     {'name':'Gani','grades':(35,47,12,50,35)},
# ]

# for student in students:
#     print(average(student["grades"]))    


# # 16
# avg=lambda seq:sum(seq)/len(seq)
# total=lambda seq:sum(seq)
# top=lambda seq:max(seq)


# students=[
#     {'name':'Rolf','grades':(50,25,30,60,90)},
#     {'name':'Sanjar','grades':(40,28,42,63,82)},
#     {'name':'Asal','grades':(25,41,78,55,75)},
#     {'name':'Gani','grades':(35,47,12,50,35)},
# ]

# for student in students:
#     name=student["name"]
#     grades=student["grades"]

#     print(f"Student :{name}")
#     operations=input("Choose 'average','total', or 'top' :")
    

#     if operations =='average':
#         print(avg(grades))
#     elif operations == 'total':
#         print(avg(grades))
#     elif operations =='top':
#         print(max(grades))        

# # # or 
 
# avg=lambda seq:sum(seq)/len(seq)
# total=lambda seq:sum(seq)
# top=lambda seq:max(seq)

# operation={
#     'average':avg,
#     "total":total,
#     "top":top,
# }

# students=[
#     {'name':'Rolf','grades':(50,25,30,60,90)},
#     {'name':'Sanjar','grades':(40,28,42,63,82)},
#     {'name':'Asal','grades':(25,41,78,55,75)},
#     {'name':'Gani','grades':(35,47,12,50,35)},
# ]

# for student in students:
#     name=student["name"]
#     grades=student["grades"]

#     print(f"Student :{name}")
#     operations=input("Choose 'average','total', or 'top' :")
    
#     operation_function=operation[operations]
#     print(operation_function(grades))
       



# # Paint Are Calculator
# import math

# def paint_calc(height,width,cover):
#     area=height*width
#     num_of_cans=math.ceil(area/cover)
#     print(f"You will need {num_of_cans} cans of paint")

# check_h=int(input("Height of the wall :"))
# check_w=int(input("Width of wall :"))
# coverage=5

# paint_calc(height=check_h,width=check_w,cover=coverage)




#Prime number checker

def check_prime(number):
    prime_number=True


    for i in range(2,number):
        if number%i==0:
            prime_number=False
    if prime_number:
        print(f"{number} is prime number")
    else:
        print(f"{number} is not prime number")             

user=int(input("Imput number: "))
check_prime(user)
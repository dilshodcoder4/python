# # while
# # 1
# is_learning=True

# while is_learning:
#     print('You are learning')



# # 2
# is_learning=True

# while is_learning:
#     print('You are learning')
#     is_learning=False

# # 3
# user_input=input("Do you want to run this program again? (yes/no) :")

# while user_input=="yes":
#     print('You are learning')
#     user_input=input('Do you wish to run the program? (yes/no):')

# print("we stopped") 

# # for loops
# 1
# friends=['Omadbek','Asliddin','Jamshid']

# for friend in friends:
#     print(friend)



# # 2
# elements=[0,1,3,4,5,6,7,8,9]    

# for x in elements:
#     print(x)

# # 3
# elements=[0,1,3,4,5,6,7,8,9]    

# for x in elements:
#     print("hello world")     

# 4
# for x in range(10):
#     print('hello world')

# 5
# for x in range(3,9):
#     print(x)

# # 6
# for x in range(2,30,4):
#     print(x)    


students =[
    {'name':"Dilshod",'age':20},
    {'name':"Asliddin",'age':12},
    {'name':"Asal",'age':17},
    {'name':"Ozoda",'age':15}, ]


for student in students:
    name=student['name']
    age=student['age']

    print(f"{name} is {age} years old")

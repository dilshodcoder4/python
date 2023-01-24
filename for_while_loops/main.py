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


# students =[
#     {'name':"Dilshod",'age':20},
#     {'name':"Asliddin",'age':12},
#     {'name':"Asal",'age':17},
#     {'name':"Ozoda",'age':15}, ]


# for student in students:
#     name=student['name']
#     age=student['age']

#     print(f"{name} is {age} years old")


# 6
# fruits=["Apple","Pear","Peach"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit+"Pie")

# Avarage Height 
# student_heights=input("Input a list of students :").split()
# for x in range(0, len(student_heights)):
#     student_heights[x]=int(student_heights[x])
# print(student_heights)    

# #sum()
# total_height=0
# for height in total_heights:
#     total_height+=height
# print(total_height)    

# #len()
# number_of_student=0
# for student in student_heights:
#     number_of_student+=1


# total_height=sum(student_heights)
# number_of_students=len(student_heights)
# average_height=round(total_height/number_of_students)
# print(average_height)

# # 7
# student_scores=input("Input a list of students :").split()
# for x in range(0, len(student_scores)):
#     student_scores[x]=int(student_scores[x])
# print(student_scores) 
# print(max(student_scores))
# print(min(student_scores))


# #max()
# highest_score=0
# for score in student_scores:
#     if score>highest_score:
#         highest_score=score
# print(f"The highest score in the class is {highest_score}")        

# #For Loop with Range
# #1
# for number in range(1,10):
#     print(number)

# #2
# for number in range(1,11):
#     print(number)

# #3
# for number in range(1,11,3):
#     print(number)    

# #4
# total=0
# for number in range(1,101):
#     total+=number
#     print(total)    


# #5
# for number in range(2,101,2):
#     print(number)
         
# #6
# total=0
# for number in range(2,101,2):
#     total+=number
# print(total)

# #7
# total2=0
# for number in range(1,101):
#     if number % 2 == 0:
#         total2+=number
# print(total2)
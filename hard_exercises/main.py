# # 13. Write a Python function that prints out the first n rows of Pascal's triangle
# def pascal_triangle(n):
#     triangle = [[1]]
#     for i in range(1, n):
#         row = [1]
#         for j in range(1, i):
#             row.append(triangle[i-1][j-1] + triangle[i-1][j])
#         row.append(1)
#         triangle.append(row)
#     for row in triangle:
#         print(row)


# # 9. Write a Python program to get the Fibonacci series between 0 and 50.
# x,y=0,1

# while y<50:
#     print(y)
#     x,y=y,x+y  


# Python program to check if the number is an Armstrong number or not
number=int(input("Enter the number that you wanna chekc :"))
sum=0
temp=number
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
    
if sum==number:
    print(f"{number} is armstrong number ")    
else:
    print(f"{number} is not armstrong nunber")    
    
    
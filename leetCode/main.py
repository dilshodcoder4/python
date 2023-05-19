# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



def sum_of_number(numbers,target):
    answer=[]
    for c in numbers:
        x=target-c
        if x in numbers:
            answer1=numbers.index(x)
            answer2=numbers.index(c)
            v=(answer1,answer2)
            
    print(list(v))


sum_of_number([1,3,4,6,4],5)
# # >>> [4,1] by Rahimov Dilshod

# list1=[1,2,3,4,5,6]
# for x in list1:
#     print(x)
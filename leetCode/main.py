# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



def sum_of_number(numbers,target):
    answer=[]
    for c in range(len(numbers)):
        x=target-numbers[c]
        if x in numbers:
            answer=[numbers[c],x]
    print(answer)  


sum_of_number([1,3,4,6,4],5)
# >>> [4,1] by Rahimov Dilshod
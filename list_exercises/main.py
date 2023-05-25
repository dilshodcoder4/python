# # 1. Write a Python program to sum all the items in a list
# # 1-way
# def sum_checker(items):
#     sum_of_all=0
#     for x in items:
#         sum_of_all+=x
        
#     print(sum_of_all)    
    
# list=[1,2,3,4,5,6,7]    
# sum_checker(list)
# #>>> 28
# # 2-way you can easly use sum() to calculate sum of all items
# list=[1,2,3,4,5,6,7]
# print(sum(list))   
# #>>> 28

# # 2. Write a Python program to multiply all the items in a list.
# def multiply(items):
#     multiply_of_all=1
#     for x in items:
#         multiply_of_all*=x
        
#     print(multiply_of_all)
# list=[1,2,3,4,5,6,7]
# multiply(list)        
# #>>>5040

# # 3. Write a Python program to get the largest number from a list. 
# # 1-way
# list=[1,2,3,4,5,6,7]
# max_score=1
# for score in list:
#     if score>=max_score:
#         max_score=score
    
# print(max_score)     
# #>>>7
# #2-way
# print(max(list))
# #>>>7


# # 4. Write a Python program to get the smallest number from a list. 
# list=[1,2,3,4,5,6,7]
# min_element=1
# for score in list:
#     if min_element>=score:
#         min_element=score
        
# print(min_element)
# #>>> 1

# # 5. Write a Python program to count the number of strings from a given list of strings.
# # The string length is 2 or more and the first and last characters are the same.
# def match_words(words):
#   string = 0
#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       string+= 1
#   return string
# print(match_words(['abc', 'xyz', 'aba', '1221']))       
# #>>> 2

# # 6. Write a Python program to get a list, 
# # sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# def last(n):
#   return n[-1]

# def sorter_list(tuples):
#   return sorted(tuples,key=last)

# print(sorter_list([(1,9),(3,8),(4,5),(2,6)]))
# # here is the answer
# # >>>[(4, 5), (2, 6), (3, 8), (1, 9)]

# # 7. Write a Python program to remove duplicates from a list.
# simple=[]
# a=int(input("Enter nuber of elements: "))
# for c in range(0,a):
#   son=int(input(": "))
#   simple.append(son)
# withoutdublicates=[]
# for x in simple:
#   if x not  in withoutdublicates:
#     withoutdublicates.append(x)
   
# print(withoutdublicates)    
# # Enter nuber of elements: 7   
# # : 1
# # : 1
# # : 4
# # : 4
# # : 5
# # : 5
# # : 7 
# # [1, 4, 5, 7]


# # 8. Write a Python program to check if a list is empty or not.
# l = []
# if not l:
#   print("List is empty")
  
  
# # 9. Write a Python program to clone or copy a list.
# list=[33,67,899,99]
# list2=[]
# list2.append(list)
# print(list)
# print(list2)
# # >>>
# # [33, 67, 899, 99]
# # [[33, 67, 899, 99]]

# # 10. Write a Python program to find the list of words that are longer than n from a given list of words.
# def list_sorter(n,str):
#   empty_list=[]
#   text=str.split(" ")
#   for x in text:
#     if len(x)>n:
#       empty_list.append(x)
#   return empty_list

# print(list_sorter(3,"hello ms i am dilshod how are you doing today"))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def checker(firststring,second):
  result=False
  for c in firststring:
      for x in  second:
        if x == c:
          result=True
          return result
    
print(checker([1,2,3,4,5], [5,6,7,8,9]))
print(checker([1,2,3,4,5], [6,7,8,9]))     
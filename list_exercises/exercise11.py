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
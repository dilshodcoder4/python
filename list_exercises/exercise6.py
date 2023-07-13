# 6. Write a Python program to get a list, 
# sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
def last(n):
  return n[-1]

def sorter_list(tuples):
  return sorted(tuples,key=last)

print(sorter_list([(1,9),(3,8),(4,5),(2,6)]))
# here is the answer
# >>>[(4, 5), (2, 6), (3, 8), (1, 9)]
# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def list_sorter(n,str):
  empty_list=[]
  text=str.split(" ")
  for x in text:
    if len(x)>n:
      empty_list.append(x)
  return empty_list

print(list_sorter(3,"hello ms i am dilshod how are you doing today"))
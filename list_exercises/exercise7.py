# 7. Write a Python program to remove duplicates from a list.
simple=[]
a=int(input("Enter nuber of elements: "))
for c in range(0,a):
  son=int(input(": "))
  simple.append(son)
withoutdublicates=[]
for x in simple:
  if x not  in withoutdublicates:
    withoutdublicates.append(x)
   
print(withoutdublicates)    
# Enter nuber of elements: 7   
# : 1
# : 1
# : 4
# : 4
# : 5
# : 5
# : 7 
# [1, 4, 5, 7]
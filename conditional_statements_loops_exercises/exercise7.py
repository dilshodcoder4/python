# 7. Write a Python program that prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for x in datalist:
    print(f"The type {x} is  {type(x)}")    
# >>>    
# The type 1452 is  <class 'int'>
# The type 11.23 is  <class 'float'>
# The type (1+2j) is  <class 'complex'>
# The type True is  <class 'bool'>
# The type w3resource is  <class 'str'>
# The type (0, -1) is  <class 'tuple'>
# The type [5, 12] is  <class 'list'>
# The type {'class': 'V', 'section': 'A'} is  <class 'dict'>    

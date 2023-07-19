# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
list=['Dilshod','Asror','Jasur','Nilufar','Sapar','Nurali']
newrr=[]
for dust in list:
    if dust=='Dilshod' or dust=='Sapar' or dust=='Nurali':
        pass
    else:
        newrr.append(dust)
        
print(newrr)

# ====>
# ['Asror', 'Jasur', 'Nilufar']
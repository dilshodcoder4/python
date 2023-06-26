# 11. Write a Python function to check whether a number is "Perfect" or not. 
def perfect_number(n):
    empty_list=[]
    for number in range(1,n):
        if n%number==0:
            empty_list.append(number)
        else:
            continue
    if sum(empty_list)==n:
        print(f"{n} is perfect number")
    else:
        print(f"{n} is not perfect number")            
        
perfect_number(496)
#>>>496 is perfect number
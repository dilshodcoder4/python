# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# This question seemed so easy for me then i decided to code of swapcase() 
def upper_lover(string):
    empty_string=""
    x=len(string)
    for i in range(x):
        if string[i] ==(string[i]).upper():
            empty_string=empty_string+(string[i]).lower()
        else:
            string[i] ==(string[i]).lower()
            empty_string=empty_string+(string[i]).upper()     
    print(empty_string)


upper_lover("hElo DilsHod")    
 
#>>> HeLO dILShOD
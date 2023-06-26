
# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
def upper_lower_counter(string):
    lower=0
    upper=0
    for x in string:
        if x==x.upper():
            upper+=1
        else:
            lower+=1
    print(f"There is {lower} lower letter(s) in the word") 
    print(f"There is {upper} upper letter(s) in the word")           
                
upper_lower_counter("hEllo")
# >>>There is 4 lower letter(s) in the word
# >>>There is 1 upper letter(s) in the word
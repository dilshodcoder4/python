# 5. Define a Python function student(). Using function attributes display the names of all arguments.
def student_info(name,id_student,country):
    return f"This student is {name},his sudent id is {id_student},{name.capitalize()} is from {country}"

print(student_info("Dilshod",2225,"Uzbekistan"))

# ====>
# This student is Dilshod,his sudent id is 2225,Dilshod is from Uzbekistan
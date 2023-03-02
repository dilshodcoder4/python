# # Dictionaries
# # >>>
# # Python provides another composite data type called a dictionary, 
# # which is similar to a list in that it is a collection of objects.
# # >>>
# # Dictionaries and lists share the following characteristics:

# # Both are mutable.
# # Both are dynamic. They can grow and shrink as needed.
# # Both can be nested. A list can contain another list. A dictionary can contain another dictionary. 
# # A dictionary can also contain a list, and vice versa.

# # >>>
# # Dictionaries differ from lists primarily in how elements are accessed:

# # List elements are accessed by their position in the list, via indexing.
# # Dictionary elements are accessed via keys.


# # >>>
# # d = {
# #     <key>: <value>,
# #     <key>: <value>,
# #       .
# #       .
# #       .
# #     <key>: <value>
# # }

# # >>>
# # MLB_team = {
# # ...     'Dilshod' : 'Yaxshi',
# # ...     'Asal'   : 'Aqilli',
# # ...     'Omadbek': 'Trishqoq',
# # ...     'Nurillo': 'Kuchli',
# # ...     'Sanjar'  : 'Mexnatkash'
# # ... }


# #>>>
# # Accessing Dictionary Values
# # Of course, dictionary elements must be accessible somehow. If you don’t get them by index, then how do you get them?

# # A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([]):

# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# print(friends_age['Asliddin'])
# #>>> 30

# # Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:
# # <<<------->>>
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# friends_age['Dilshod']=20
# print(friends_age)


# # To delete an entry, use the del statement, specifying the key to delete:

# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# del friends_age['Omadbek']
# print(friends_age)


# #>>>
# # clear()-lears a dictionary.

# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# friends_age.clear()
# print(friends_age)
# # >>> {}

# #>>>
# # get()-Returns the value for a key if it exists in the dictionary.
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# print(friends_age.get("Asliddin"))
# # >>> 30

# # >>>
# # items()-returns a list of key-value pairs in a dictionary.
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# print(list(friends_age.items()))
# # >>>[('Asliddin', 30), ('Asal', 20), ('Omadbek', 15)]

# # >>>
# # keys()-Returns a list of keys in a dictionary.
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# print(list(friends_age.keys()))
# # >>>['Asliddin', 'Asal', 'Omadbek']

# # >>>
# # values()-Returns a list of values in a dictionary.
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# print(list(friends_age.values()))
# # >>>[30, 20, 15]


# # >>>
# # pop(<key>[, <default>])-Removes a key from a dictionary, if it is present, and returns its value.
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# friends_age.pop("Asliddin")
# print(friends_age)
# # >>>{'Asal': 20, 'Omadbek': 15}


# # >>>
# # popitem()-Removes a key-value pair from a dictionary.
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# friends_age.popitem()
# print(friends_age)
# #>>>{'Asliddin': 30, 'Asal': 20}

# # >>>
# frineds=[('Asliddin', 30), ('Asal', 20), ('Omadbek', 15)]
# for friend in frineds:
#     print(friend)


# # >>>
# frineds=[('Asliddin', 30), ('Asal', 20), ('Omadbek', 15)]
# for name, age in frineds:
#     print(name,age)


# Iterating over dictionaries 
# # >>>
# frineds=[('Asliddin', 30), ('Asal', 20), ('Omadbek', 15)]
# for name in frineds:
#     print(name)    
    
# # >>>    
# frineds={'Asliddin': 30, 'Asal': 20, 'Omadbek': 15}
# for age in frineds.values():
#     print(age)   
        
# # >>>        
# frineds={'Asliddin': 30, 'Asal': 20, 'Omadbek': 15}
# for name, age in frineds.items():
#     print(f"{name} is {age} years old")       




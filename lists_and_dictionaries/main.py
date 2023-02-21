# # Lists
# # <<<------->>>
# friends=["Sanjar","Omadbek","Asal"]
# print(friends[0])
# #>>>Sanjar

# # <<<------->>>
# friends=["Sanjar","Omadbek","Asal"]
# print(len(friends))
# #>>> 3

# # <<<------->>>
# friends=[["Sanjar",20],["Omadbek",22],["Asal",15]]
# print(friends[0][0])
# #>>>Sanjar



# #Tuples
# # <<<------->>>
# friends=("Sanjar","Omadbek","Asal")
# print(friends)
# #>>>('Sanjar', 'Omadbek', 'Asal')


# # <<<------->>>
# friends=("Sanjar","Omadbek","Asal")
# friends=friends+("Nurillo",)
# print(friends)
# #>>>('Sanjar', 'Omadbek', 'Asal', 'Nurillo')


# #Sets
# # <<<------->>>
# friends={"Sanjar","Omadbek","Asal"}
# print(friends)
# #>>>{'Asal', 'Omadbek', 'Sanjar'}

# # <<<------->>>
# friends={"Sanjar","Omadbek","Asal"}
# friends.add("Barno")
# print(friends)

# #>>>{'Asal', 'Sanjar', 'Barno', 'Omadbek'}

# # Advanced Set operations

# # <<<------->>>
# friends={"Sanjar","Omadbek","Asal"}
# group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}

# friends_not_group_matess=group_mates.difference(friends)
# print(friends_not_group_matess)
# #>>>{'Asliddin', 'Barno'}

# # <<<------->>>
# friends={"Sanjar","Omadbek","Asal"}
# group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}
# not_in_both=group_mates.symmetric_difference(friends)
# print(not_in_both)
# #>>>{'Asliddin', 'Barno'}

# # <<<------->>>
# friends={"Sanjar","Omadbek","Asal"}
# group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}
# in_both=group_mates.intersection(friends)
# print(in_both)
# #>>>{'Omadbek', 'Sanjar', 'Asal'}


# # <<<------->>>
# friends={"Sanjar","Omadbek","Asal"}
# group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}
# all_friends=group_mates.union(friends)
# print(all_friends)
# #>>>{'Barno', 'Asliddin', 'Omadbek', 'Asal', 'Sanjar'}


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


# popitemda qoldim 




# # <<<------->>>
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# print(friends_age["Omadbek"])
# #>>> 15


# # <<<------->>>
# friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
# friends_age["Asal"]=18
# friends_age["Omadbek"]=16
# print(friends_age)
# #>>>{'Asliddin': 30, 'Asal': 18, 'Omadbek': 16}

# # <<<------->>>
# cars=({"make":"Ford","model":"Fiesta","mileage":2300, "fuel_consumed":456},
#      {"make":"Bugatti","model":"Chevrolet","mileage":200, "fuel_consumed":120},
#      {"make":"Ferrari","model":"Daewoo","mileage":800, "fuel_consumed":200},
#      {"make":"Nexia","model":"Chevrolet_2","mileage":1200, "fuel_consumed":750})

# print(cars[0]["make"])
# print(cars[1]["make"])
# print(cars[2]["make"])
# print(cars[3]["make"])

# #>>>Ford
# #>>>Bugatti
# #>>>Ferrari
# #>>>Nexia



# friends=[("Asliddin",30),("Asal",20),("Omadbek",13)]
# friends_age=dict(friends)
# print(friends_age)
# #>>>{'Asliddin': 30, 'Asal': 20, 'Omadbek': 13}


# # Length and sum

# grades=[20,30,12,15,74]
# print(sum(grades))
# #>>> 151
# grades=[20,30,12,15,74]
# print(len(grades))
# #>>> 5
# total=sum(grades)
# length=len(grades)

# average=total/length
# print(average)
# #>>> 30.2

# #Join
# friends=['Omadbek',"Ozodbek","Sardor"]
# comma_separated=",".join(friends)
# print(f"My friends{comma_separated}.")
# #>>> My friendsOmadbek,Ozodbek,Sardor.

# #List slicing in Python
# friends=['Omadbek',"Ozodbek","Sardor","Asal","Nurillo"]
# print(friends[2:4])
# #>>> ['Sardor', 'Asal']

# friends=['Omadbek',"Ozodbek","Sardor","Asal","Nurillo"]
# print(friends[2:])
# #>>>['Sardor', 'Asal', 'Nurillo']

# friends=['Omadbek',"Ozodbek","Sardor","Asal","Nurillo"]
# print(friends[:3])
# #>>>['Omadbek', 'Ozodbek', 'Sardor']


# #List comprehension
# numbers=[20,12,2,3,6]
# doubled_numbers=[]
# for x in numbers:
#     doubled_numbers.append(x*2)

# print(doubled_numbers)    

# #>>>[40, 24, 4, 6, 12]

# # shorter way
# doubled_numbers=[number*2 for number in numbers]
# print(doubled_numbers)
# #>>>[40, 24, 4, 6, 12]

# doubled_numbers=[number*2 for number in range(5)]
# print(doubled_numbers)
# #>>>[0, 2, 4, 6, 8]

# friends_age=[12,15,19,23,19]
# age_strings=[f"My friend is {age} years old " for age in friends_age]
# print(age_strings)
# #>>>['My friend is 12 years old ', 'My friend is 15 years old ',
# #    'My friend is 19 years old ', 'My friend is 23 years old ', 
# #    'My friend is 19 years old ']


# # <<<------->>>
# names=['Omadbek', 'Ozodbek', 'Sardor']
# lower=[name.lower() for name in names]
# print(lower)
# #>>>['omadbek', 'ozodbek', 'sardor']

# # <<<------->>>
# friend=input("Enter your friend name :")
# friends=['Omadbek',"Ozodbek","Sardor","Asal","Nurillo"]
# friends_lower=[name.lower() for name in friends]

# if friend.lower() in friends_lower:
#     print(f"{friend.title()} is one of your friend")

# #>>> Enter your friend name :omadbek
# #>>> Omadbek is one of your friend    

# #Comprehension with conditionals
# ages=[20,12,32,14,26,53,11]
# odds=[ age for age in ages if age %2==1]
# print(odds)
# #>>>[53, 11]

# # <<<------->>
# friends=['Omadbek',"ozodbek","Sardor","asal","Nurillo"]
# guests=['omadbek',"Asilbek","sardor","Davron","nurillo"]
# friends_lower=set([friend.lower() for friend in friends ])
# guests_lower=set([guest.lower() for guest in guests ])

# print(friends_lower.intersection(guests_lower))
# #>>>{'omadbek', 'nurillo', 'sardor'}

# # <<<------->>
# friends=['Omadbek',"ozodbek","Sardor","asal","Nurillo"]
# guests=['omadbek',"Asilbek","sardor","Davron","nurillo"]
# friends_lower=set([friend.lower() for friend in friends ])

# present_friends=[
#     name.title() 
#     for name in guests 
#     if name.lower() in friends_lower
#     ]

# print(present_friends)    
#>>>['Omadbek', 'Sardor', 'Nurillo']

# # Set and dictionary comprehensionda 

# # <<<------->> dilshodcoder
# friends=['Omadbek',"ozodbek","Sardor","asal","Nurillo"]
# guests=['omadbek',"Asilbek","sardor","Davron","nurillo"]
# # here you can do :
# # 1-way
# friends_lower=set(n.lower() for n in friends)
# guests_lower=set(n.lower for n in guests)
# # 2-way so we  use 2 nd way beacuse it is easier 
# friends_lower={n.lower() for n in friends}
# guests_lower={n.lower() for n in guests}


# present_friends={name.title() for name in friends_lower.intersection(guests)}

# print(present_friends)

# # <<<------->>dilshodcoder
# friends=["Masha","Oliver","Rose","Steve"]
# time_since_seen=[3,7,25,11]
# long_timers={
#     friends[i]:time_since_seen[i]
#     for i in range(len(friends))
#     if time_since_seen[i] > 5
# }
# print(long_timers)

# # >>>{'Oliver': 7, 'Rose': 25, 'Steve': 11}

# # <<<------->>dilshodcoder
# friends=["Masha","Oliver","Rose","Steve"]
# time_since_seen=[3,7,25,11]
# long_timers=dict(zip(friends,time_since_seen))
# print(long_timers)

# # <<<------->>dilshodcoder
# friends=["Masha","Oliver","Rose","Steve"]
# time_since_seen=[3,7,25,11]
# long_timers=dict(zip(friends,time_since_seen))
# print(long_timers)
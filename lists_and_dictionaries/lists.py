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

# present_friends=[
#     name.title() 
#     for name in guests 
#     if name.lower() in friends_lower
#     ]

# print(present_friends)    
#>>>['Omadbek', 'Sardor', 'Nurillo']

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
# #>>>{'Masha': 3, 'Oliver': 7, 'Rose': 25, 'Steve': 11}

#List methods

# Lists
# <<<------->>>
friends=["Sanjar","Omadbek","Asal"]
print(friends[0])
#>>>Sanjar

# <<<------->>>
friends=["Sanjar","Omadbek","Asal"]
print(len(friends))
#>>> 3

# <<<------->>>
friends=[["Sanjar",20],["Omadbek",22],["Asal",15]]
print(friends[0][0])
#>>>Sanjar



#Tuples
# <<<------->>>
friends=("Sanjar","Omadbek","Asal")
print(friends)
#>>>('Sanjar', 'Omadbek', 'Asal')


# <<<------->>>
friends=("Sanjar","Omadbek","Asal")
friends=friends+("Nurillo",)
print(friends)
#>>>('Sanjar', 'Omadbek', 'Asal', 'Nurillo')


#Sets
# <<<------->>>
friends={"Sanjar","Omadbek","Asal"}
print(friends)
#>>>{'Asal', 'Omadbek', 'Sanjar'}

# <<<------->>>
friends={"Sanjar","Omadbek","Asal"}
friends.add("Barno")
print(friends)

#>>>{'Asal', 'Sanjar', 'Barno', 'Omadbek'}

# Advanced Set operations

# <<<------->>>
friends={"Sanjar","Omadbek","Asal"}
group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}

friends_not_group_matess=group_mates.difference(friends)
print(friends_not_group_matess)
#>>>{'Asliddin', 'Barno'}

# <<<------->>>
friends={"Sanjar","Omadbek","Asal"}
group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}
not_in_both=group_mates.symmetric_difference(friends)
print(not_in_both)
#>>>{'Asliddin', 'Barno'}

# <<<------->>>
friends={"Sanjar","Omadbek","Asal"}
group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}
in_both=group_mates.intersection(friends)
print(in_both)
#>>>{'Omadbek', 'Sanjar', 'Asal'}


# <<<------->>>
friends={"Sanjar","Omadbek","Asal"}
group_mates={"Sanjar","Omadbek","Asal","Barno","Asliddin"}
all_friends=group_mates.union(friends)
print(all_friends)
#>>>{'Barno', 'Asliddin', 'Omadbek', 'Asal', 'Sanjar'}


# Dictionaries
# <<<------->>>
friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
print(friends_age["Omadbek"])
#>>> 15


# <<<------->>>
friends_age={"Asliddin":30,"Asal":20,"Omadbek":15}
friends_age["Asal"]=18
friends_age["Omadbek"]=16
print(friends_age)
#>>>{'Asliddin': 30, 'Asal': 18, 'Omadbek': 16}

# <<<------->>>
cars=({"make":"Ford","model":"Fiesta","mileage":2300, "fuel_consumed":456},
     {"make":"Bugatti","model":"Chevrolet","mileage":200, "fuel_consumed":120},
     {"make":"Ferrari","model":"Daewoo","mileage":800, "fuel_consumed":200},
     {"make":"Nexia","model":"Chevrolet_2","mileage":1200, "fuel_consumed":750})

print(cars[0]["make"])
print(cars[1]["make"])
print(cars[2]["make"])
print(cars[3]["make"])

#>>>Ford
#>>>Bugatti
#>>>Ferrari
#>>>Nexia



friends=[("Asliddin",30),("Asal",20),("Omadbek",13)]
friends_age=dict(friends)
print(friends_age)
#>>>{'Asliddin': 30, 'Asal': 20, 'Omadbek': 13}


# Length and sum

grades=[20,30,12,15,74]
print(sum(grades))
#>>> 151
grades=[20,30,12,15,74]
print(len(grades))
#>>> 5
total=sum(grades)
length=len(grades)

average=total/length
print(average)
#>>> 30.2

#joing listda qoldim 
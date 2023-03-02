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



# # <<<------->>
# friends=['Omadbek',"ozodbek","Sardor","asal","Nurillo"]
# guests=['omadbek',"Asilbek","sardor","Davron","nurillo"]
# friends_lower=set([friend.lower() for friend in friends ])
# guests_lower=set([guest.lower() for guest in guests ])

# print(friends_lower.intersection(guests_lower))
# #>>>{'omadbek', 'nurillo', 'sardor'}
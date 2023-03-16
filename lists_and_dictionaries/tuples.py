# #Tuples
# <<<------->>>
friends=("Sanjar","Omadbek","Asal")
print(friends)
#>>>('Sanjar', 'Omadbek', 'Asal')


# <<<------->>>
friends=("Sanjar","Omadbek","Asal")
friends=friends+("Nurillo",)
print(friends)
#>>>('Sanjar', 'Omadbek', 'Asal', 'Nurillo')


# Change values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
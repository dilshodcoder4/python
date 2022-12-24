import sys, random
print('Welcome to game !!!')
FirstName = "jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
"ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
"ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
"lydia", "charles", "pedro", "bradley"
LastName = "barker", "style", "spirits", "murphy", "blacker", "bleacher", "rogers",
"warren", "keller"

while True:
    firstname=random.choice(FirstName)

    lastName=random.choice(LastName)

    print('\n\n')
    print("{}{}".format(firstname,lastName),file=sys.stderr)    
    print('\n\n')

    try_again=input("\n\nTry again?\n\nPress  quit to exist: ")
    if try_again.lower() == 'q':
        break
    input("\nPress Enter to exit ")



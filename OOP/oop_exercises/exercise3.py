# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class My_friend:
    def __init__(self,name,age,weight,favourite_song):
        self.name=name
        self.age=age
        self.weight=weight
        self.favourite_song=favourite_song
        
my_first_friend=(My_friend("Omadbek",12,45,"jayron"))  
print(my_first_friend.__dict__)      
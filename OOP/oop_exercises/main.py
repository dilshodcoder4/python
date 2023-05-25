# # 1. Write a Python program to import a built-in array module and display the namespace of the said module.
# import array
# for name in array.__dict__:
#     print(name)
    
# # __name__
# # __doc__
# # __package__
# # __loader__
# # __spec__
# # _array_reconstructor
# # __file__
# # ArrayType
# # array
# # typecodes    
 
# # 2. Write a Python program to create a class and display the namespace of that class.
 
# class py_solution:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))    
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
#         return [current]
# for name in py_solution.__dict__:
#     print(name)
    
# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.
class My_friend:
    def __init__(self,name,age,weight,favourite_song):
        self.name=name
        self.age=age
        self.weight=weight
        self.favourite_song=favourite_song
        
my_first_friend=(My_friend("Omadbek",12,45,"jayron"))  
print(my_first_friend.__dict__)      
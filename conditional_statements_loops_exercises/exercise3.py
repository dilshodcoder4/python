# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
# on successful guess, user will get a "Well guessed!" message, and the program will exit.
import random
numbers=[1,2,3,4,5,6,7]
random_number=random.choice(numbers)
user_guess_number=int(input("Imput the number"))
while True:
    if user_guess_number==random_number:
        print("Correct")
        break
    else:
        print("Uncorrect Please Try again : Yes/No :")
        user_choise=(input(":"))
        if user_choise=="Yes":
            user_guess_number=int(input("Imput the number"))
        else:
            break

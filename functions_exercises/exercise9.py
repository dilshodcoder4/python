# 9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def check_prime(number):
    prime_number=True


    for i in range(2,number):
        if number%i==0:
            prime_number=False
    if prime_number:
        print(f"{number} is prime number")
    else:
        print(f"{number} is not prime number")             

user=int(input("Imput number: "))
check_prime(user)
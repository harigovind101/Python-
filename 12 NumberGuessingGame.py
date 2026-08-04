#Program picks a random number; user guesses with 'too high/too low' hints until correct. Upload as guessing_game.py.
import random

print("welcome to number guessing game")
print("please enter a number between 1 and 100")
random_number = random.randint(1, 100)
num = int(input("enter a number: "))

while num != random_number:
    if num < random_number:
        print("too low")
    elif num > random_number:
        print("too high")

    num = int(input("enter a number: "))

print("congrats you got the number")
print("DONE")
    
    

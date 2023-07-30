import random 
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Crear una lista de números del 1 al 100
list_of_numbers = list(range(1,101))

random_number = random.choice(list_of_numbers)

if difficulty.lower() == "easy":
    print("You have selected easy mode. You have 10 attempts remaining to guess the number.")
    attemps = 10
elif difficulty.lower() == "hard":
    print("You have selected hard mode. You have 5 attempts remaining to guess the number.")
    attemps = 5
else:
    print("You must be typing somenthing wrong!!")

def guessing_game():
    global attemps
    stop = False
    while not stop:
        if attemps == 0:
            print(f"Sorry you have no attemps remaining so you loose.")
            break 
        
        print("Guess again.")
        guess = int(input("Make a guess: "))
      
        if guess == random_number:
            print("OMG You win!!")
            stop = True
        elif guess < random_number:
            print("Too low.")
            attemps -= 1
            print(f"You have {attemps} remaining to guess the number.")
        elif guess > random_number:
            print("Too high.")
            attemps -= 1
            print(f"You have {attemps} remaining to guess the number.")


guessing_game()
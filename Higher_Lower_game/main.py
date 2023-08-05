import random 
from art import logo, vs
from game_data import data
from os import system



lose = False
score = 0

while not lose:
    choice_A = random.choice(data) if score == 0 else choice_B
    choice_B = random.choice(data)
    print(logo)

    if score >= 1:
        print(f"You are right!!🙋‍♂️🙋‍♀️ Current score is {score}")

    if choice_A == choice_B:
        choice_C = random.choice(data)
        choice_B = choice_C

    print(f"Compare A: {choice_A['name']}, {choice_A['description']}, {choice_A['country']}")
    print(vs)
    print(f"Against B: {choice_B['name']}, {choice_B['description']}, {choice_B['country']}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    if user_choice.lower() == "a":
        if choice_A['follower_count'] > choice_B['follower_count']:
            score += 1
            choice_A = choice_B
            system('cls')
        else:
            lose = True
    else:
        if choice_B['follower_count'] > choice_A['follower_count']:
            score += 1
            choice_A = choice_B
            system('cls')
        else:
            lose = True

system('cls')
print(logo)
print(f'Sorry that is wrong. Final score: {score}')
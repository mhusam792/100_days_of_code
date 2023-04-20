from art import logo, vs
from game_data import data
import random
from replit import clear

def rand_choice(data):
    random.choice()

print(logo)
a = rand_choice(data)
b = rand_choice(data)

if b == a:
    b = rand_choice(data)

score = 0

def name(choice, class_choice):
    print(f"Compare {class_choice}: {choice['name']}, a {choice['description']}, from {choice['country']}.")

game_on = True
while game_on:

    def correct_choice():
        global score, a, b
        score += 1
        a = b
        b = rand_choice(data)
        if b == a:
            b = rand_choice(data)
        clear()
        print(f"You're right! Current score: {score}")

    def wrong_chice():
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        global game_on
        game_on = False

    # number of followers for each random choice
    a_follower_count = a['follower_count']
    b_follower_count = b['follower_count']

    name(a, 'A')
    print(vs)
    name(b, 'B')

    print(a_follower_count)
    print(b_follower_count)
    
    # handling user input and make user choice 'A' or 'B'
    user_input = True
    choices = ['a', 'b']
    while user_input:
        choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
        if choice in choices:
            user_input = False
        else:
            print("please enter 'A' or 'B'\n")

    if choice == 'a':
        if a_follower_count > b_follower_count:
            correct_choice()
            continue
        else:
            wrong_chice()
    else:
        if b_follower_count > a_follower_count:
            correct_choice()
            continue
        else:
            wrong_chice()

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

choices = ['hard', 'easy']
difficulty = input("Choose a difficulty. Type'easy' or 'hard': ").strip().lower()

# handling the input of difficulty it it was not 'hard' or 'easy'
while difficulty not in choices:
        print("Please enter difficulty level bettwen 'hard' or 'easy'.\n")
        difficulty = input("Choose a difficulty. Type'easy' or 'hard': ").strip().lower()

if difficulty == 'easy':
    num_attempts = 10
elif difficulty == 'hard':
    num_attempts = 5

# generate a random number
rand_num = random.randint(1, 100)

while num_attempts > 0:
    print(f"You have {num_attempts} attempts remaining to guess the number.")

    # handling the guessing number if it was a string
    num_type = True
    while num_type:
        try:
            guessing = int(input("Make a guess: "))
            num_type = False
        except:
            print("please inter a number not strings\n")
            continue
    
    if rand_num == guessing:
        print(f"You got it! The answer was {rand_num}")
        print("Guess a gain.")
        break
    elif guessing > rand_num:
        print("Too high.")
    else:
        print("Too low.")

    num_attempts -= 1
    if num_attempts == 0:
        print("You've run out of guesses, You lose.")

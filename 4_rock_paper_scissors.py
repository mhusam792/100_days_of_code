rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_list = [rock, paper, scissors]
play_again = "yes"
print("Welcome to Rock, Paper and Scissors Game.")
print(rock, paper, scissors)

while play_again == "yes":
    # try except
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    except ValueError:
        print("Please Type 0 for Rock, 1 for Paper or 2 for Scissors.")
        continue
    
    # printing user choice
    print(user_choice)
    print(game_list[user_choice])

    # printing random choice
    print("Computer chose:")
    rand_choice = random.choice(range(len(game_list)))
    print(game_list[rand_choice])

    # conditional state for the game
    if user_choice == 0 and rand_choice == 2:
        print("You win.")
    elif user_choice == 0 and rand_choice == 1:
        print("You lose.")
    elif user_choice == 1 and rand_choice == 0:
        print("You win.")
    elif user_choice == 1 and rand_choice == 2:
        print("You lose.")
    elif user_choice == 2 and rand_choice == 1:
        print("You win.")
    elif user_choice == 2 and rand_choice == 0:
        print("You lose.")
    else:
        print("Draw.")
    
    play_again = input("Do you want to play again? Type 'yes' to play again or Type any letter to Exit.").lower()
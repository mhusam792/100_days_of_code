# Need to update code and handling errors

import random 
from art import logo
from replit import clear

def rand_num():
    ls = list()
    for x in range(2):
        ls.append(random.randint(1, 10))
    return ls

def check_cards(card):
    if 11 in card and sum(card) > 21:
        user.remove(11)
        user.append(1)
    elif 1 in card and sum(card) <= 11:
        user.remove(1)
        user.append(11)

def print_this():
    print(f"    Your final hand: {user}, final score: {sum(user)}")
    print(f"    Computer's final hand: {dealer}, findal score: {sum(dealer)}")

game_on = True
while game_on:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    user = rand_num()
    dealer = rand_num()
    
    if play == 'y':
        clear()
        print(logo)
        user = rand_num()
        dealer = rand_num()
        again = True

    elif play == 'n':
        again = False

    while again:
        print(user, dealer)
        print(user)

        if 11 in user and sum(user) > 21:
            user.remove(11)
            user.append(1)
        elif 1 in user and sum(user) <= 11:
            user.remove(1)
            user.append(11)

        print(f"    You cards: {user}, current score {sum(user)}")
        print(f"    Computer's first card: {dealer[0]}")

        if sum(user) == 21: 
            print_this()
            print("You win.")
            break
        elif sum(dealer) == 21:
            print_this()
            print("You lose.")
            break
        elif sum(user) > 21:
            print_this()
            print("You lose.")
            break

        card_or_pass = input("Type 'y' to get another card, Type'n' to pass: ")

        if card_or_pass == 'y':
            user.append(random.randint(1, 10))
            continue
        elif card_or_pass == 'n':
            while sum(dealer) <= 17:
                dealer.append(random.randint(1, 10))
                if 11 in dealer and sum(dealer) > 11:
                    dealer.remove(11)
                    dealer.append(1)
                elif 1 in dealer and sum(dealer) <= 11:
                    dealer.remove(1)
                    dealer.append(11)
        
        check_cards(dealer)
        check_cards(user)

        print_this()

        if sum(user) == 21: 
            print("You win.")
        elif sum(dealer) == 21:
            print("You lose.")
        elif sum(user) > 21:
            print("You lose.")
        elif sum(dealer) > 21:
            print("You win.")
        elif sum(user) > sum(dealer):
            print("You win.")
        elif sum(user) < sum(dealer):
            print("You lose.")
        else:
            print("Draw")

        again = False

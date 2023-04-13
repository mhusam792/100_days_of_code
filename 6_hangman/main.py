from hangman_art import logo, stages
from hangman_words import word_list
import random

print(logo)

rand_word = random.choice(word_list)
print(rand_word)
# random word and under score word
list_letter = []
under_score_word = []
for letter in rand_word:
    list_letter.append(letter)
    under_score_word.append("_")

def list_duplicates_of(seq,item):
    """Return the indexes of specific item"""
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


num_lives = 6
num_statge = -1
while num_lives > 0:
    
    letter = input("Guess a letter: ")
    list_duplicates = list_duplicates_of(list_letter, letter)
    word = " ".join(under_score_word)

    if letter in word:
        print(f"You have already guessed {letter}")

    if letter in list_letter:
        for x in list_duplicates:
            under_score_word[x] = letter
            word = " ".join(under_score_word)

    else:
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        num_lives -= 1
        num_statge -= 1

    
    print(word)
    print(stages[num_statge])


    if "_" not in under_score_word:
        print("You win.")
        break

    if num_lives == 0:
        print("You lose.")

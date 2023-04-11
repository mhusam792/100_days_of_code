#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

is_int = False
while is_int == False:
    try:
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        is_int = True
    except ValueError:
        print("Please Type just numbers not letters")
        continue


def pass_generator(list, range_num):
    ls_letters = []
    for letter in range(range_num):
        ls_letters.append(random.choice(list))
    return (ls_letters)

rand_letters = pass_generator(letters, nr_letters)
rand_numbers = pass_generator(numbers, nr_numbers)
rand_symbols = pass_generator(symbols, nr_symbols)

print(rand_letters, rand_numbers, rand_symbols)

list_pass = rand_numbers + rand_letters + rand_symbols
random.shuffle(list_pass)
print("Your new password is: ")
print(''.join(list_pass))
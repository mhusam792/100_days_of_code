from replit import clear
from art import logo

print(logo)
dictionary = dict()

again = True
while again:
    name = input("What is your name?: ").lower().strip()
    num_type = True
    while num_type:
        try:
            bid = float(input("What is your bid?: $"))
            num_type = False
        except:
            print("please inter a number not strings")
            continue
    
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()

    dictionary[name] = bid

    if other_bidders == "no":
        again = False
    else:
        clear()

sorted_dict = sorted([(v,k) for k, v in dictionary.items()], reverse= True)
name = sorted_dict[0][1]
bid = sorted_dict[0][0]

print(f"The winner is {name} with a bid of ${bid}")
    

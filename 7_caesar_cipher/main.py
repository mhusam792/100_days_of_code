alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet += alphabet

from art import logo
print(logo)

def caesar_cipher(text, shift, direction):
    """This function is to encrypt a message consisting of letters and numbers"""
    ls_letter = []

    while shift > len(alphabet):
        shift -= len(alphabet)

    for letter in text:
        if direction == "encode":
            cipher = alphabet.index(letter) + shift
        else:
            cipher = alphabet.index(letter) - shift

        ls_letter.append(alphabet[cipher])
    decode_text = "".join(ls_letter)
    return f"Here's the encoded result: {decode_text}"

play_on = True
while play_on:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Note: please type letters or numbers not a symbols\n Type your message: ").lower().strip()
    shift = int(input("Type the shift number:\n"))

    encripting = caesar_cipher(text, shift, direction)
    print(encripting)
    
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if play_again == 'no':
        play_on = False
    

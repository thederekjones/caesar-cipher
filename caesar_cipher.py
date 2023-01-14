#!/usr/bin/python3

from alphabet_list import alphabet
from art import logo


print(logo)


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ""

    if cypher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            end_text += alphabet[alphabet.index(char) + shift_amount]
        else:
            end_text += char

    print(f"The {cypher_direction}d text is: {end_text}")


restart_cipher = True

while restart_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cypher_direction=direction)

    restart = input(
        "Do you want to restart the program? Type 'yes' or 'no' now.\n"
    ).lower()

    if restart == "no":
        restart_cipher = False

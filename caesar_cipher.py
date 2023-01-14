#!/usr/bin/python3

from alphabet_list import alphabet
from art import logo


print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ""

    if cypher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter in alphabet:
            end_text += alphabet[alphabet.index(letter) + shift_amount]
        else:
            end_text += letter

    print(f"The {cypher_direction}d text is: {end_text}")


caesar(start_text=text, shift_amount=shift, cypher_direction=direction)

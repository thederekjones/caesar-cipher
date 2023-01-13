#!/usr/bin/python3

from alphabet_list import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    encrypted_text = ""

    for letter in plain_text:
        encrypted_text += alphabet[alphabet.index(letter) + shift_amount]

    print(f"The encoded text is: {encrypted_text}")


def decrypt(plain_text, shift_amount):
    decrypted_text = ""

    for letter in plain_text:
        decrypted_text += alphabet[alphabet.index(letter) - shift_amount]

    print(f"The decrypted text is: {decrypted_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)
else:
    print("That wasn't a valid choice!")

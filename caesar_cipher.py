from alphabet_list import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""

    for letter in plain_text:
        cipher_text += alphabet[alphabet.index(letter) + shift_amount]

    print(f"The encoded text is {cipher_text}")


encrypt(plain_text=text, shift_amount=shift)

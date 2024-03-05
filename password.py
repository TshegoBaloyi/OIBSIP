import random
import string

length = int(input("Enter the desired password length: "))
include_letters = input("Include letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

characters = ""
if include_letters:
    characters += string.ascii_letters
if include_numbers:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

password = "".join(random.choice(characters) for _ in range(length))
print("Generated Password:", password)


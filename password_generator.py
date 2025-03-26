import random
import string
import pyperclip  # For copying password to clipboard

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type!"

    # Generate password from selected character types
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    # Ask user for password length
    length = int(input("Enter the desired password length: "))
    
    # Ask what character types to include
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        password = generate_password(length, include_letters, include_digits, include_symbols)
        print("Generated password:", password)
        
        # Copy to clipboard
        pyperclip.copy(password)
        print("Password has been copied to your clipboard!")
        
except ValueError:
    print("Please enter a valid number.")
""" List of functions used for Random Password Generator """
import random as rand
import password_limit_exception as ple
from password_limit_exception import PasswordLimitError

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_chars = '!@#$%&*^|()_+-'

def generate_password(length):

    count = 1
    sequences = {}
    password = []

    # Building a Dictionary based what sequences the user wants to use
    use_upper = True if input('Use uppercase letters? (y/n): ') == 'y' else False
    use_digits = True if input('Use digits? (y/n): ') == 'y' else False
    use_special = True if input('Use special characters? (y/n): ') == 'y' else False

    sequences[count] = lowercase
    if use_upper == True:
        count += 1
        sequences[count] = uppercase

    if use_digits == True:
        count += 1
        sequences[count] = digits

    if use_special == True:
        count += 1
        sequences[count] = special_chars

    # If no other sequences are selected
    if count == 1: 
        password = rand.choices(lowercase, k=length)
    else:
        for _ in range(length):
            seq_to_use = rand.randint(1, count)     # Randomly accesing diffrent sequences
            password.append(rand.choice(sequences[seq_to_use]))

    return ''.join(password)

# Set Password Length
def set_password_length():
    while True:     #continue looping until the user provides a valid length
        try:
            length = int(input('Provide password length: '))
        except ValueError:
            print('ValueError: must be an integer')
        else:
            try:
                valid_length = ple.valid_range(length)
            except PasswordLimitError:
                print('PassswordLimitError: Length of password must be between 8 and 20')
            else:
                print(f'Password length is {valid_length}')
                return valid_length

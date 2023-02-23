""" This program generates a random password """
import random as rand

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_chars = '!@#$%&*^|()_+-'

while True:
    
    try:
        print('-- Password Generator --' , 'Choose option:', '1: generate password',
'2: exit the program', sep='\n') 

        selected_option = int(input('Your choice: '))
    except ValueError:
        print('ValueError: Your response should be 1 or 2')
    else:
        if selected_option == 1:
            # password = generate_password()
            print('Generated password:', 'password')
        else:
            print('Bye!')
            break

    

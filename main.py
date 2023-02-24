""" The main program for Random Password Generation """
import functions as rpg_fun

# Starts program
while True:
    print('-- Password Generator --' , 'Choose option:', '1: generate password',
'2: exit the program', sep='\n') 

    try:
        selected_option = int(input('Your choice: '))
    except ValueError:
        print('Invalid Option: Your response should be 1 or 2')
    else:
        if selected_option == 1:
            length = rpg_fun.set_password_length()
            print(type(length))
            password = rpg_fun.generate_password(length)
            print('Generated password:', password)
        elif selected_option == 2:
            print('Bye!')
            break
        else:
            print('Invalid Option: Your response should be 1 or 2')

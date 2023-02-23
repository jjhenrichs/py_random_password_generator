""" This program generates a random password """

while True:
    
    try:
        print('-- Password Generator --' , 'Choose option:', '1: generate password',
'2: exit the program', sep='\n') 

        selected_option = int(input('Your choice: '))
    except ValueError:
        print('ValueError: Your response should be 1 or 2')
    else:
        if selected_option == 2:
            print('Bye!')
            break

    

""" This is a custom exception that returns a string if the length of the password is less than 
8 characters or greater than 20 characters. """

class PasswordLimitError(Exception):
    """ your password must be somewhere between 8 to 20 charcters"""
    min_length = 8
    max_length = 20

    def __init__(self, length, *args):
        super().__init__(args)
        self.length = length

    def __str__(self):
       return f'Password length {self.length} should be {self.min_length} to {self.max_length} characters long.'

def valid_range(length):
    if length < PasswordLimitError.min_length or length > PasswordLimitError.max_length:
        raise PasswordLimitError(length)

    return length

if __name__ == '__main__':
    
    try:
        length = int(input('Enter a password length: '))
    except ValueError:
        print('ValueError: Must be an integer')
    else:
        try:
            valid_length = valid_range(length)
        except PasswordLimitError as ple:
            print(ple)
        else:
            print(f'Password length is {length}')

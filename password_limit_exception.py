""" This is a custom exception """

class PasswordLimitException(Exception):
    """ your password must be somewhere between 8 to 20 charcters"""
    min_length = 8
    max_length = 20

    def __init__(self, length, *args):
        super().__init__(args)
        self.length = length

    def __str__(self):
        if self.length > self.max_length:
            return f'Password length should be no more than {self.max_length} characters long.'
        else:
            return f'Password length must be at least {self.min_length} characters long.'

try:
    raise PasswordLimitException(21)
except PasswordLimitException as p:
    print(p)
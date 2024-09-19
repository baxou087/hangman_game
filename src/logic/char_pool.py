import json

CHAR_LIST = ['A','B','C','D','E','F',
                'G','H','I','J','K','L',
                'M','N','O','P','Q','R',
                'S','T','U','V','W','X',
                'y','Z']

class char_pool:

    # will contain the char_pool A -> Z
    _cp          = {}


    '''
        char_pool constructor

        returns : void
    '''
    def __init__(self):
        for char in CHAR_LIST:
            self._cp[char] = True




    '''
        Method used to make a character visible to the player

        returns : void
    '''
    def enable_char(self, char):
        if char in CHAR_LIST:
            self._cp[char] = False




    '''
        Method used to make a character non visible to the player

        returns : void
    '''
    def disable_char(self, char):
        if char in CHAR_LIST:
            self._cp[char] = False




    '''
        Method used to know if the character is visible or not to the player

        returns : bool
    '''
    def is_visible(self, char):
        return self._cp[char]




    '''
        Method to print the char pool to the terminal

        returns : void
    '''
    def to_string(self):
        print(json.dumps(self._cp, indent=4))
import json

CHAR_LIST = ['A','B','C','D','E','F',
             'G','H','I','J','K','L',
             'M','N','O','P','Q','R',
             'S','T','U','V','W','X',
             'Y','Z']

class letter_pool:

    # Will contain a dict containing the letter_pool A -> Z
    # Each letter will be associated to a boolean.
    # The boolean will be used to know if the letter
    # will be shown to the player or not
    _lp             = None




    '''
        letter_pool constructor

        Parameter:  str
        Returns:    None
    '''
    def __init__(self):
        self._lp = CHAR_LIST.copy()




    '''
        Method used to get the letters the player can buy
        We do not return the letters the players has already bought

        Parameter:  None
        Returns:    None
    '''
    def get_letter_pool(self):
        return self._lp




    '''
        Method used to make a letter non visible to the player

        Parameter:  str
        Returns:    None
    '''
    def disable_letter(self, letter):
        self._lp.remove(letter)




    '''
        Method used to know if the letter is visible or not to the player

        Parameter:  str
        Returns:    bool
    '''
    def is_visible(self, letter: str) -> bool:
        return letter in self._lp




    '''
        Method to print the letter pool to the terminal

        Parameter:  None
        Returns:    None
    '''
    def to_string(self):
        print(json.dumps(self._lp, indent=4))
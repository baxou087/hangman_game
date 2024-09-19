import random


class word_pool:

    # list containing the word_pool
    _wp = []
    # String containing the path to the file containing the words to load
    _fp = ""


    '''
    Constructor

    Returns: void
    '''
    def __init__(self, file_path):
        self._fp = file_path
        self.load_word_pool()




    '''
    Method used to load the word_pool

    Returns: void
    '''
    def load_word_pool(self):
        self._wp = open(self._fp).read().splitlines()




    '''
    Method used return a random word from the word_pool

    Returns: String
    '''
    def get_word(self) -> str:
        word = ""
        size = len(self._wp)

        # if the word_pool is exhausted, it is reloaded
        if size == 0:
            self.load_word_pool()
            size = len(self._wp)

        # getting a random word from the word pool
        # removing it from the list
        rng  = random.randrange(0, size)
        word = self._wp[rng]
        del self._wp[rng]

        return word


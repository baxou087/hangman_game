import random


class word_pool:

    # list containing the word_pool
    _wp = []
    # size of the word_pool
    _sz = 0
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
        print("word_pool reloaded")
        self._wp = open(self._fp).read().splitlines()
        self._sz = len(self._wp)




    '''
    Method used return a random word from the word_pool

    Returns: String
    '''
    def get_word(self) -> str:
        word = ""

        # if the word_pool is exhausted, it is reloaded
        if self.is_empty():
            self.load_word_pool()
            self._sz = len(self._wp)

        # getting a random word from the word pool
        # removing it from the list
        rng         = random.randrange(0, self._sz)
        word        = self._wp[rng]
        self._sz   -= 1
        del self._wp[rng]

        return word




    '''
        Method used to test the word pool reloading

        Returns : a boolean to know if the word_pool is empty
    '''
    def is_empty(self) -> bool:
        return self._sz == 0




    '''
        Method used to test the word pool reloading
    '''
    def test_get_word(self):
        for i in range(0, 10):
            print(self.get_word())




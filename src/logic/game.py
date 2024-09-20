from word_pool              import *
from letter_pool            import *


class game:

    # Will contain the word_pool
    _wp     = None

    # Will contain the letter_pool
    _lp     = None

    # Will contain the word to find
    _word   = ""

    # Will contain the number of points available to the player.
    # The players needs points to be able to buy letters from the game.
    # If the number of points falls to 0, the game is over.
    _currency = 0

    # Will contain the number of words found by the player
    _score  = 0




    '''
        Constructor

        Parameter:  str
        Returns:    None
    '''
    def __init__(self, file_path) -> None:
        self._wp        = word_pool(file_path)
        self._lp        = letter_pool()
        self._currency  = 0
        self._score     = 0




    '''
        Method used for knowing if the game is over
        The game is considered as over when the player gets negative currency

        Parameter:  None
        Returns:    bool
    '''
    def game_over(self) -> bool:
        return self._currency < 0




    '''
        Method used for updating the player's score.
        The score is the number number of words found by the player
        Since the player tries to find only one word at a time,
        we only increment it by one when the player finds a word

        Parameter:  None
        Returns:    None
    '''
    def update_score(self):
        self._score += 1




    '''
        Method used for updating the player's currency.
        The currency is the ressource used by the player to buy letters
        from the game. He loses one currency if the letter he bought doesn't
        exist in the word to find. Otherwise they get a number of points
        equal to the number of occurrences the bought letter appears.

        Said otherwise if the player choses the letter 'E' and it appears 3
        times in the word, then the player gets 3 points of currency.
        But if the letter 'W' doesn't appear in the word, then the player loses
        one currency

        Parameter:  int
        Returns:    None
    '''
    def update_currency(self, points: int):
        self._currency += points




    '''
        Method used to check if the letter bought by the player is in the word.
        The method will return a set with all the indexes where the bought letter appears.

        parameter:  str
        Returns:    set
    '''
    def is_letter_in_word(self, letter: str) -> set:
        res = set()

        for i, char in enumerate(self._word):
            if letter == char:
                res.add(i)

        return res





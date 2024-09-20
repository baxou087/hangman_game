from logic.word_pool              import *
from logic.letter_pool            import *

import os


STARTING_POINTS = 3
MAX_CURRENCY    = 4
QUIT_GAME       = "QQ"
SPACE           = " "
DASH            = "-"
NO_CHAR         = ""
MASKED_LETTER   = "_ "


class game:

    # Will contain the word_pool
    _wp             = None

    # Will contain the letter_pool
    _lp             = None

    # Will contain the letters tried by the player
    _lt             = None

    # Will contain the word to find
    _word           = ""

    # Will contain the number of points available to the player.
    # The players needs points to be able to buy letters from the game.
    # If the number of points falls to 0, the game is over.
    _currency       = 0

    # Will contain the number of words found by the player
    _score          = 0




    '''
        Constructor

        Parameter:  str
        Returns:    None
    '''
    def __init__(self, file_path) -> None:
        self._wp        = word_pool(file_path)
        self._lp        = letter_pool()
        self._lt        = set()
        self._currency  = STARTING_POINTS
        self._score     = 0




    '''
        Method running the game

        Parameter:  None
        Returns:    None
    '''
    def run(self):
        # We get the new word the player must find
        self._word              = self._wp.get_word()
        word_length             = len(self._word.replace(DASH, NO_CHAR))
        nb_characters_found     = 0

        # Main loop of the game
        while not self.game_over():

            #Displaying the current state of the game
            self.display_game()

            # Asking the player the letter they want to buy
            letter  = ""
            l_pool  = self._lp.get_letter_pool()
            while letter not in l_pool:
                letter = input(f"--\nWhat letter do you wish to buy (input {QUIT_GAME} to quit the game) ? ")
                letter = letter.upper()

                # Checking if the players wants to quit the game
                if letter == QUIT_GAME:
                    exit()

            # We add the letter input from the player in the set of letters
            # bought by the player and we disable said letter
            self._lt.add(letter)
            self._lp.disable_letter(letter)

            # Checking if the letter is in the word to find
            points                  = self.nb_times_letter_in_word(letter)
            nb_characters_found    += points
            self.update_currency(points)

            # Checking if the word has been found
            if word_length == nb_characters_found:
                print(f"\nWell done! The word was \"{self._word}\"")
                input("Press enter to get the next word")

                # Updating the player's score
                self.update_score()

                # Resetting the bought letters set
                self.reset_letter_pool()

                # Getting a new word and its length
                self._word  = self._wp.get_word()
                word_length = len(self._word)

                # resetting the number of characters found
                nb_characters_found   = 0


        print("\nGame Over !")
        print(f"The word you were looking for was : \"{self._word}\"")
        print(f"You found a total of {self._score} words !\n")
        exit()




    '''
        Method used to display the state of game

        Parameter:  None
        Returns:    None
    '''
    def display_game(self):
        letters_to_display  = ""
        for char in self._word:
            if char in self._lt or char == DASH:
                letters_to_display += char + SPACE
            else:
                letters_to_display += MASKED_LETTER

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"Words found    = {self._score}")
        print(f"Currency       = {self._currency} / {MAX_CURRENCY}")
        print(f"\nWord_to_find : {letters_to_display}")
        #print(f"word : {self._word}")
        print(f"\nLetters left : {self._lp.get_letter_pool()}")




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

        In order to not make the game too easy, the player cannot get more than
        a maximum currency

        Parameter:  int
        Returns:    None
    '''
    def update_currency(self, points: int):
        if points == 0:
            self._currency -= 1
        else:
            self._currency += points
            if self._currency > MAX_CURRENCY:
                self._currency = MAX_CURRENCY




    '''
        Method that returns the number of times the letter is in the word

        parameter:  str
        Returns:    int
    '''
    def nb_times_letter_in_word(self, letter: str) -> int:
        return self._word.count(letter)




    '''
        Method used to reset the letter_pool and the pool of letters tried
        used when the player has found the word.

        parameter:  None
        Returns:    None
    '''
    def reset_letter_pool(self):
        self._lp = letter_pool()
        self._lt = set()




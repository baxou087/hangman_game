from logic.word_pool              import *
from logic.letter_pool            import *

import os


STARTING_POINTS = 4
MAX_CURRENCY    = 20

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
    _found          = 0

    # Will contain the player's score.
    # The lesser mistakes the player makes, the higher the score
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
        self._found     = 0




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
        while not self.game_lost():

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
                self.display_game()
                print(f"\nWell done!")
                input("\nPress enter to get the next word")

                # Updating the number of words found
                self.update_found()

                # If the game is won we break the loop
                if self.game_won():
                    print("\nCongratulation ! You have won !")
                    break

                # Resetting the bought letters set
                self.reset_letter_pool()

                # Getting a new word and its length
                self._word  = self._wp.get_word()
                word_length = len(self._word)

                # resetting the number of characters found
                nb_characters_found   = 0


        if self.game_lost():
            print("\nGame Over !")
            print(f"The word you were looking for was : \"{self._word}\"")
            print(f"You found a total of {self._found} words !\n")
            print(f"You got a score of {self._currency}/{MAX_CURRENCY} !\n")




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

        print(f"Words found    = {self._found}")
        print(f"Currency       = {self._currency} / {MAX_CURRENCY} (Win the game by getting {MAX_CURRENCY} or more)")
        print(f"\nWord_to_find : {letters_to_display}")
        #print(f"word : {self._word}")

        lt = sorted(self._lt) if len(self._lt) > 0 else "{}"
        print(f"\nLetters tried : {lt}")

        print(f"Letters left  : {self._lp.get_letter_pool()}")




    '''
        Method used for knowing if the game is over
        The game is considered as over when the player gets negative currency

        Parameter:  None
        Returns:    bool
    '''
    def game_over(self) -> bool:
        return self.game_lost() or self.game_won()




    '''
        Method used for knowing if the game is won
        The game is considered as won if the player's has
        max currency or more

        Parameter:  None
        Returns:    bool
    '''
    def game_won(self) -> bool:
        return self._currency >= MAX_CURRENCY




    '''
        Method used for knowing if the game is lost
        The game is considered as lost when the player gets
        to zero currency or less

        Parameter:  None
        Returns:    bool
    '''
    def game_lost(self) -> bool:
        return self._currency <= 0




    '''
        Method used for updating the number of words the player has found.
        Since the player tries to find only one word at a time,
        we only increment it by one when the player finds a word

        Parameter:  None
        Returns:    None
    '''
    def update_found(self):
        self._found += 1




    '''
        Method used for updating the number of words the player has found.
        Since the player tries to find only one word at a time,
        we only increment it by one when the player finds a word

        Parameter:  None
        Returns:    None
    '''
    def update_score(self):
        self._score += self._currency




    '''
        Method used for updating the player's currency.
        The currency is both the player's score and the ressource
        the player uses to buy letters from the game.
        He loses one currency if the letter he bought doesn't
        exist in the word to find. Otherwise the player gets 1 point.

        Parameter:  int
        Returns:    None
    '''
    def update_currency(self, points: int):
        pt = -1 if points == 0 else 1
        self._currency += pt




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




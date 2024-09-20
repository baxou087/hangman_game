from logic.game               import *

FILE_PATH       = "../files/mots"
FILE_PATH_TEST  = "../files/test"

if __name__ == "__main__":
#    new_game = game(FILE_PATH_TEST)
    while True:
        new_game = game(FILE_PATH)
        new_game.run()

        answer = ""
        while answer not in ["Y", "N"]:
            answer = input("\nPlay again (Y or N) ? ")
            answer = answer.upper()

        if answer == "N":
            exit()
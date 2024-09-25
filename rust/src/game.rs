use crate::{letter_pool::LetterPool, word_pool::WordPool};
use text_io::read;

const STARTING_CURRENCY:    u32  = 4;
const MAX_CURRENCY:         u32  = 20;
const FIRST_TIER:           u32  = 10;
const SECOND_TIER:          u32  = 15;
const ONE:                  u32  = 1;
const TWO:                  u32  = 2;
const THREE:                u32  = 3;


const QUIT_GAME:            &str = "QQ";

pub struct Game {
    word:       String,
    lp:         LetterPool,
    wp:         WordPool,
    currency:   u32,
    found:      u32
}


impl Game {

    /// Constructor for the main structure of the game
    pub fn new() -> Game {
        Game {
            word:       String::new(),
            lp:         LetterPool::new(),
            wp:         WordPool::new(),
            currency:   STARTING_CURRENCY,
            found:      0
        }
    }

    /// Main loop of the game
    pub fn run(self: &mut Self) {

        self.word = self.wp.get_word();

        'main_loop: loop {
            self.display_game();

            // ask the player to input a letter and check if the letter has been bought.
            // if not loop until the player enters a letter that can be bought
            loop {
                // checking if the word has been found
                if self.has_been_found() {
                    self.found += 1;
                    // Checking if the winning condition has been met
                    if self.game_won() { 
                        break 'main_loop;
                    }

                    // preparing the next word
                    self.word = self.wp.get_word();
                    self.lp = LetterPool::new();
                    self.display_game();
                }

                // checking if the player lost the game (no currency left)
                if self.lose_condition() {
                    self.game_over_display();
                    break 'main_loop;
                }

                // asking the player what letter they want to buy
                let input = self.ask_for_user_input();

                // checking if the player wants to quit the game
                if input == QUIT_GAME { break 'main_loop; }

                // checking if the letter is available
                let letter: char = input.chars().nth(0).unwrap();
                if self.lp.is_letter_available(letter) {
                    self.lp.buy_letter(letter);

                    // checking if the letter is in the word
                    // and calculating the new currency value
                    if self.is_in_word(letter) {
                        self.currency += 1;
                    } else {
                        match self.currency {
                            0..FIRST_TIER           => self.currency -= ONE,
                            FIRST_TIER..SECOND_TIER => self.currency -= TWO,
                            _                       => self.currency -= THREE
                        }
                    }
                    break;
                }

            }



        }
    }


    ///Displays the game to the player
    pub fn display_game(self: &Self) {
        // print!("{esc}[2J{esc}[1;1H", esc = 27 as char); 
        println!("Words found   : {}", self.found);
        println!("Currency      : {} / {} (Win the game by getting 20 or more)", self.currency, MAX_CURRENCY);
        println!("");
        println!("Word to find  : {}", self.display_word());
        println!("Word to find  : {}", self.word);
        println!("");
        println!("Bought        : {}", LetterPool::display_letter_pool(self.lp.bought()));
        println!("Available     : {}", LetterPool::display_letter_pool(self.lp.available()));
    }


    pub fn game_over_display(&self) {
        println!("\nGame Over !");
        println!("The word you were looking for was : \"{}\"", self.word);
        println!("\nPress enter to continue");
        let mut buffer = String::new();
        let _ = std::io::stdin().read_line(&mut buffer);
    }


    /// Displays a word on the terminal depending on
    /// the letters that have been bought by the player
    /// 
    /// If the word contains the '-' character, then it is displayed as is
    /// 
    pub fn display_word(self: &Self) -> String {
        let mut s: String = String::from("");
        let bought: &Vec<char> = self.lp.bought();
        for c in self.word.chars() {
            if c == '-' {
                s.push_str(&String::from(" - "));
            } else if bought.contains(&c) {
                s.push_str(&String::from(c));
                s.push_str(&String::from(" "));
            } else {
                s.push_str(&String::from("_ "));
            }
        }

        s
    }


    /// Asks the player to either buy a letter (A to Z) or input "QQ" to quit the game
    ///
    /// If the player inputs anything else, then the game will loop until a valid
    /// input is passed
    pub fn ask_for_user_input(&self) -> String {
        let mut input: String;

        loop {
            print!("What letter do you wish to buy (input QQ to quit the game) ? ");
            input = read!();
            input = input.to_uppercase();

            // quitting the game
            if input == "QQ" {
                break;
            }

            // valid input condition
            let valid_input: bool = input.len() == 1 &&
                            (input.chars().nth(0).unwrap() >= 'A' &&
                             input.chars().nth(0).unwrap() <= 'Z');

            if valid_input {
                break;
            }
        }

        input
    }



    /// Checks if the word has been found by the player.
    pub fn has_been_found(&self) -> bool {
        let bought_letters = self.lp.bought();

        // we remove the '-' char before checking the word has been found
        let wrd = self.word.replace("-", "");

        wrd.chars().all(|c| bought_letters.contains(&c))
    }


    /// Checks if the player has won the game.
    ///
    /// The only way for the player to win a game is to have
    /// currency equal to MAX_CURRENCY or more
    pub fn game_won(&self) -> bool {
        self.currency >= MAX_CURRENCY
    }


    /// Checks if the player has lost the game.
    ///
    /// The only way for the player to lose a game is to have
    /// no currency left.
    pub fn lose_condition(&self) -> bool {
        self.currency <= 0
    }


    /// Checks if the letter is in the word the player must guess
    pub fn is_in_word(&self, letter: char) -> bool {
        self.word.contains(letter)
    }


}


//#[cfg(test)]
//mod tests {
//use crate::game::Game;
//
//}

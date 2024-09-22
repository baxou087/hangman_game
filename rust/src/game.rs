use crate::{letter_pool::LetterPool, word_pool::WordPool};

const STARTING_CURRENCY:    u32 = 4;
const MAX_CURRENCY:         u32 = 20;


pub struct Game {
    word:       String,
    lp:         LetterPool,
    wp:         WordPool,
    currency:   u32,
    found:      u32
}


impl Game {

    /// Constructor for the main structure of the game
    pub fn new(filepath: String) -> Game {
        Game {
            word:       String::new(),
            lp:         LetterPool::new(),
            wp:         WordPool::new(filepath),
            currency:   STARTING_CURRENCY,
            found:      0
        }
    }


    pub fn run(self: &mut Self) {
        self.word = self.wp.get_word();
        self.display_game();
    }


    ///Displays the game to the player
    pub fn display_game(self: &Self) {
        print!("{esc}[2J{esc}[1;1H", esc = 27 as char); 
        println!("Words found   : {}", self.found);
        println!("Currency      : {} / {} (Win the game by getting 20 or more)", self.currency, MAX_CURRENCY);
        println!("");
        println!("Word to find  : {}", self.display_word());
        println!("Word to find  : {}", self.word);
        println!("");
        println!("Bought        : {}", Game::display_letter_pool(self.lp.bought()));
        println!("Available     : {}", Game::display_letter_pool(self.lp.available()));
    }


    /// Displays the letter pool that has been passed as an argument
    /// 
    /// If the letter_pool is empty, the method returns "[]"
    /// 
    /// If the letter_pool contains A, B and C, it return "[ A ; B ; C ]"
    /// 
    /// # Example
    /// ```
    ///    let v1: Vec<char> = Vec::new();
    ///    assert_eq!(Game::display_letter_pool(v1), "[]");
    ///    let v2: Vec<char> = vec!['A', 'B', 'C'];
    ///    assert_eq!(Game::display_letter_pool(v2), "[ A ; B ; C ]");
    /// ```
    pub fn display_letter_pool(lp: Vec<char>) -> String {
        if lp.len() == 0 {
            String::from("[]")
        } else {
            let sz = lp.len() - 1;

            let mut s: String = String::from("[ ");
            for (i, c) in lp.iter().enumerate() {
                s.push_str(&c.to_string());
                if i != sz {s.push_str(" ; ");}
            }
            s.push_str(" ]");

            s
        }
    }


    /// Displays a word on the terminal depending on
    /// the letters that have been bought by the player
    /// 
    /// If the word contains the '-' character, then it is displayed as is
    /// 
    pub fn display_word(self: &Self) -> String {
        let mut s: String = String::from("");
        let bought: Vec<char> = self.lp.bought();
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




}


#[cfg(test)]
mod tests {
use crate::game::Game;

    #[test]
    fn test_display_letter_pool() {
        let v1: Vec<char> = Vec::new();
        assert_eq!(Game::display_letter_pool(v1), "[]");
        let v2: Vec<char> = vec!['A', 'B', 'C'];
        assert_eq!(Game::display_letter_pool(v2), "[ A ; B ; C ]");
    }
}

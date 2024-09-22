use crate::{letter_pool::LetterPool, word_pool::WordPool};

const STARTING_CURRENCY:    u32 = 4;
const MAX_CURRENCY:         u32 = 20;


pub struct Game {
    word:       String,
    to_find:    String,
    lp:         LetterPool,
    wp:         WordPool,
    currency:   u32,
    found:      u32
}


impl Game {

    pub fn new(filepath: String) -> Game {
        Game {
            word:       String::new(),
            to_find:    String::new(),
            lp:         LetterPool::new(),
            wp:         WordPool::new(filepath),
            currency:   STARTING_CURRENCY,
            found:      0
        }
    }



    ///Displays the game to the player
    pub fn display_game(self: &Self) {
        println!("Words found   : {}", self.found);
        println!("Currency      : {} / {} (Win the game by getting 20 or more)", self.currency, MAX_CURRENCY);
        println!("");
        println!("Word to find  : {}", self.to_find);
        println!("");
        println!("Bought        : {}", Game::display_letter_pool(self.lp.bought()));
        println!("Availablec    : {}", Game::display_letter_pool(self.lp.available()));
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


mod letter_pool;
mod word_pool;
mod game;

use crate::game::Game;

use text_io::read;


fn main() {
    'game_loop: loop {
        let mut game: Game = Game::new();
        game.run();

        'input: loop {
            print!("\nPlay again (Y/N) ? ");
            let input: String = read!();

            match input.chars().nth(0).unwrap().to_ascii_uppercase() {
                'N' => { break 'game_loop; }
                'Y' => { break 'input; }
                _   => { continue; }
            }
        }

    }
}

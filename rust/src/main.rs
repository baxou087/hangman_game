
mod letter_pool;
mod word_pool;
mod game;

use crate::game::Game;

const FILEPATH: &str = "../files/mots";


fn main() {
    let game: Game = Game::new(FILEPATH.to_string());
    game.display_game();
}

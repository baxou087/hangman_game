
mod letter_pool;
mod word_pool;
mod game;

use crate::game::Game;



fn main() {
    let mut game: Game = Game::new();
    game.run();
}

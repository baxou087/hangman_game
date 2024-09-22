

extern crate rand;
use rand::Rng;



pub struct WordPool {
    word_pool: Vec<String>,
    file_path: String,
    size:      usize
}


impl WordPool {


    /// Constructor of the WordPool structure
    ///
    /// It requires a file_path to a file containing the words the player will have to find.
    /// 
    /// ```
    ///    let wp: WordPool = WordPool::new(FILEPATH);
    ///
    ///    assert_eq!(wp.word_pool.contains(&"ZONES".to_string()), true);
    ///    assert_eq!(wp.word_pool.contains(&"ZOO-LOGIE".to_string()), true);
    ///    assert_eq!(wp.word_pool.contains(&"ZOZOTER".to_string()), true);
    ///    assert_eq!(wp.word_pool.contains(&"ZYGOTE".to_string()), true);
    ///
    /// ```
    pub fn new(filepath: String) -> WordPool{
        WordPool{
            file_path: filepath,
            word_pool: Vec::new(),
            size: 0
        }
    }


    /// Opens and reads the file containing the words into a vector of strings
    pub fn load_word_pool(self: &mut Self) {
        use std::fs;

        let err_msg = format!("file {} wasn't found", self.file_path);
        let contents = fs::read_to_string(self.file_path.clone())
            .expect(&err_msg);

        self.word_pool = contents.split_whitespace().map(str::to_string).collect();

        self.size = self.word_pool.len();
    }



    /// This method returns a random word from the word_pool,
    /// that the player will have to find.
    /// 
    /// This word will be taken out of the word_pool so that it won't be
    /// picked a second time.
    /// 
    /// # Example
    /// ```
    ///    const WORD_LIST: [&str; 4] = ["ZONES", "ZOO-LOGIE", "ZOZOTER", "ZYGOTE"];
    ///
    ///    let mut wp: WordPool = WordPool::new(FILEPATH.to_string());
    ///
    ///    for _ in 0..wp.size {
    ///        assert_eq!(WORD_LIST.contains(&wp.get_word().as_str()), true);
    ///    }
    ///
    ///    // testing one last time to make sure the file is reloaded
    ///    assert_eq!(WORD_LIST.contains(&wp.get_word().as_str()), true);
    /// ```
    pub fn get_word(self: &mut Self) -> String {
        // if the word_pool is empty, then we reload it
        if self.is_empty() {
            self.load_word_pool();
        }

        let mut rng = rand::thread_rng();
        let n: u32 = rng.gen_range(0..self.size as u32);
        println!("{}", n);

        self.size -= 1;

        self.word_pool.swap_remove(n as usize)
    }


    /// This method returns true if the word_pool is empty, false otherwise
    ///
    /// # Example
    /// ```
    ///    let mut wp: WordPool = WordPool::new(FILEPATH);
    ///
    ///    let wl = WORD_LIST.len(); 
    ///    let wp_size = wp.word_pool.len();
    ///    for i in 0..wp_size {
    ///        let size = wp.word_pool.len();
    ///        assert_eq!(size, wl - i);
    ///        assert_eq!(WORD_LIST.contains(&wp.get_word().as_str()), true);
    ///    }
    ///    // testing one last time to make sure the file is reloaded
    ///    assert_eq!(WORD_LIST.contains(&wp.get_word().as_str()), true);
    /// ```
    pub fn is_empty(self: &Self) -> bool {
        self.size == 0
    }


}


#[cfg(test)]
mod tests {
    use super::WordPool;

    const FILEPATH: &str = "../files/test";

    #[test]
    fn test_new() {
        let wp: WordPool = WordPool::new(FILEPATH.to_string());

        assert_eq!(wp.word_pool.len(), 0);
    }


    #[test]
    fn test_is_empty() {
        let mut wp: WordPool = WordPool::new(FILEPATH.to_string());

        assert_eq!(wp.is_empty(), true);
        wp.load_word_pool();
        assert_eq!(wp.is_empty(), false);

    }


    #[test]
    fn test_get_word() {
        const WORD_LIST: [&str; 4] = ["ZONES", "ZOO-LOGIE", "ZOZOTER", "ZYGOTE"];

        let mut wp: WordPool = WordPool::new(FILEPATH.to_string());

        for _ in 0..wp.size {
            assert_eq!(WORD_LIST.contains(&wp.get_word().as_str()), true);
        }

        // testing one last time to make sure the file is reloaded
        assert_eq!(WORD_LIST.contains(&wp.get_word().as_str()), true);
    }

}
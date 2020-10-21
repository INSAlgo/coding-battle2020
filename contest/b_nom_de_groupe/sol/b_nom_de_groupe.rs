// Solution by Thomas Lacroix

fn main() {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    let name = line.trim();

    let n_vowels = name
        .chars()
        .filter(|c| ['a', 'e', 'i', 'o', 'u', 'y'].contains(c))
        .count() as i32;
    let n_consonants = name.len() as i32 - n_vowels;

    let mut score: i32 = 2 * n_vowels - n_consonants + if name.contains("ker") { 5 } else { 0 };
    if score > 0 && name.chars().eq(name.chars().rev()) {
        score *= 2
    }

    println!("{}", score);
}

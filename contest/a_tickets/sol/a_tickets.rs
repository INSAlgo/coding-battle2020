// Solution by Thomas Lacroix

use std::io;

fn read_int() -> i32 {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn main() {
    let n = read_int();
    let p1 = read_int();
    let p2 = read_int();
    let p3 = read_int();

    let sum = if n > 200 {
        (n - 200) * p3 + 100 * p2 + 100 * p1
    } else if n > 100 {
        (n - 100) * p2 + 100 * p1
    } else {
        n * p1
    };
    println!("{}", sum);
}

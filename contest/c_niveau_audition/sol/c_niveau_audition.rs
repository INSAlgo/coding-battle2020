// Solution by Thomas Lacroix

use std::fmt::Debug;

fn read<T: std::str::FromStr>() -> T
where
    T::Err: Debug,
{
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn read_list<T: std::str::FromStr>() -> Vec<T>
where
    T::Err: Debug,
{
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().split(" ").map(|s| s.parse().unwrap()).collect()
}

fn main() {
    let _ = read::<u32>();
    let mut rows = read_list::<u32>();
    let _ = read::<u32>();
    let mut hearing_levels = read_list::<u32>();
    hearing_levels.sort();

    let mut row = 0;
    let mut possible = true;
    'outer: for person in 0..hearing_levels.len() {
        while rows[row] == 0 {
            if row + 1 == rows.len() {
                possible = false;
                break 'outer;
            }
            row += 1
        }

        if row + 1 > hearing_levels[person] as usize {
            possible = false;
            break 'outer;
        }

        rows[row] -= 1;
    }

    println!("{}POSSIBLE", if possible { "" } else { "IM" });
}

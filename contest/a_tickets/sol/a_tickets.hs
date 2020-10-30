module Main where

getPrice :: Int -> Int -> Int -> Int -> Int
getPrice n p1 p2 p3
    | n<=100 = n*p1
    | n<=200 = 100*p1 + (n-100)*p2
    | otherwise = 100*(p1 + p2) + p3*(n-200)

main :: IO ()
main = do
    n <- readLn
    p1 <- readLn
    p2 <- readLn
    p3 <- readLn
    putStr $ show $ getPrice n p1 p2 p3

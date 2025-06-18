main = do
    putStrLn "Hello, everbody!"
    putStrLn ("Please look at my favourite odd numbers: " ++ show (filter odd [10..20]))
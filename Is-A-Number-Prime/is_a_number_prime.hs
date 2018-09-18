isPrime :: Integer -> Bool
isPrime x
  | x <= 1 = False
  | otherwise = all (\y -> mod x y > 0) [2..limit]
  where
    limit = round $ sqrt $ fromIntegral x

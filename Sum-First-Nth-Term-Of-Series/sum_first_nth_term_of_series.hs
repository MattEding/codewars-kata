linear :: Num a => a -> a -> a-> a
linear slope yint x = slope * x + yint

roundTwoDec :: RealFloat a => a -> String
roundTwoDec x = showFFloat (Just 2) x ""

seriesSum :: Integer -> String
seriesSum x = roundTwoDec (sum $ map (\x -> transform x) $ [0..x-1])
  where
    transform x = recip $ fromIntegral $ linear 3 1 x

solution :: Integer -> String
solution n = formatRoman $ toRoman n

formatRoman :: String -> String
formatRoman (a:b:c:d:xs)
  | (take 4 $ repeat a) == [a,b,c,d] = (fromJust $ lookup a dict) ++ xs
  where
    dict = [('C', "CD"), ('X', "XL"), ('I', "IV")]
formatRoman (x:xs) = x : formatRoman xs
formatRoman "" = ""

toRoman :: Integer -> String
toRoman n
  | n ==        0 = ""
  | n - 1000 >= 0 =       'M' : solution (n - 1000)
  | n -  900 >= 0 = 'C' : 'M' : solution (n - 900)
  | n -  500 >= 0 =       'D' : solution (n - 500)
  | n -  100 >= 0 =       'C' : solution (n - 100)
  | n -   90 >= 0 = 'X' : 'C' : solution (n - 90)
  | n -   50 >= 0 =       'L' : solution (n - 50)
  | n -   10 >= 0 =       'X' : solution (n - 10)
  | n -    9 >= 0 = 'I' : 'X' : solution (n - 9)
  | n -    5 >= 0 =       'V' : solution (n - 5)
  | n -    1 >= 0 =       'I' : solution (n - 1)

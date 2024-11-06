module TryingFriday where

import Vision.Image.HSV

toBlackAndWhite :: (Image i, Convertible i Grey) => i -> Grey
toBlackAndWhite img =
  let grey = convert img :: Grey
   in map (\pix -> if pix > 127 then 255 else 0) grey

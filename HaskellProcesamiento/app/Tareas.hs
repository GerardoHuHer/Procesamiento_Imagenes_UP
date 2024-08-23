module Tareas where

import Codec.Picture

imagenNegativo :: FilePath -> IO ()
imagenNegativo path = do
  eImg <- readImage path
  case eImg of
    Left err -> putStrLn $ "Error: " ++ err
    Right dynImg -> do
      let img = convertRGB8 dynImg
      let negativoImg = pixelMap (\(PixelRGB8 r g b) -> PixelRGB8 (255 - r) (255 - g) (255 - b)) img
      savePngImage "negativo.png" (ImageRGB8 negativoImg)
      putStrLn "Imagen negativa guardada como negativo.png"

blancoNegro :: FilePath -> IO ()
blancoNegro path = do
  eImg <- readImage path
  case eImg of
    Left err -> putStrLn $ "Error: " ++ err
    Right dynImg -> do
      let img = convertRGB8 dynImg
      let blancoNegroImg = pixelMap (\(PixelRGB8 r g b) -> let gray = round (fromIntegral (r + g + b) / 3) in PixelRGB8 gray gray gray) img
      savePngImage "blancoNegro.png" (ImageRGB8 blancoNegroImg)
      putStrLn "Imagen en blanco y negro guardada como blancoNegro.png"

randomColor :: FilePath -> Int -> IO ()
randomColor path num = do
  eImg <- readImage path
  case eImg of
    Left err -> putStrLn $ "Error: " ++ err
    Right dynImg -> do
      let numAux = fromIntegral (num `mod` 255)
      let img = convertRGB8 dynImg
      let random = pixelMap (\(PixelRGB8 r g b) -> PixelRGB8 (r - numAux) (g - numAux) (b - numAux)) img
      savePngImage "random.png" (ImageRGB8 random)
      putStrLn "Imagen guardada con éxito"

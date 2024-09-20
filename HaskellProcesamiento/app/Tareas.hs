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

-- Signature de la función segmentacion que recibe un tipo de dato FilePath y nos devuelve un Input Output
segmentacion :: FilePath -> IO ()
segmentacion path = do
  -- Leemos el archivo con la función readImage
  eImg <- readImage path
  -- Validamos que la imagen eImg no haya generado error al leer el archivo
  case eImg of
    Left err -> putStrLn $ "Error: " ++ err
    Right dynImg -> do
      -- Convierte la imagen a un RGB de 8 bits por canal
      let img = convertRGB8 dynImg
      -- Creación de la imagen Blanca
      let imagenBlanca = pixelMap (\(PixelRGB8 r g b) -> PixelRGB8 255 255 255) img
      savePngImage "imgaenBlanca.png" (ImageRGB8 imagenBlanca)
      -- Mapeo de los canales donde validamos para los colores azulados
      let segmento = pixelMap (\(PixelRGB8 r g b) -> if (b < 112 && b > 63) && (g < 112 && g > 10) then PixelRGB8 r g b else PixelRGB8 255 255 255) img
      -- Guardado de la foto cómo segmentacion.png
      savePngImage "segmentacion.png" (ImageRGB8 segmento)
      -- Input de salida validando que se haya guardado con éxito
      putStrLn "Imagen guardada con éxito"

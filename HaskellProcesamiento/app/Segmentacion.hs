module Segmentacion where

import Codec.Picture

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

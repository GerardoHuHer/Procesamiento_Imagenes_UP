module TareaIluminacion where

import Codec.Picture

cambiarPixel :: Double -> PixelRGB8 -> PixelRGB8
cambiarPixel factor (PixelRGB8 r g b) = do
  PixelRGB8 (ajustarBrill r) (ajustarBrill g) (ajustarBrill b)
  where
    ajustarBrill :: Pixel8 -> Pixel8
    ajustarBrill x = fromIntegral $ min 255 (max 0 (round (fromIntegral x * factor)))

cambiarBrillo :: Double -> Image PixelRGB8 -> Image PixelRGB8
cambiarBrillo factor = pixelMap (cambiarPixel factor)

runTareaIluminacion :: String -> IO ()
runTareaIluminacion path = do
  eImg <- readImage path
  case eImg of
    Left err -> putStrLn $ "Error al cargar la imagen: " ++ err
    Right dynamicImg -> do
      let img = convertRGB8 dynamicImg
      let aumentado = cambiarBrillo 1.5 img
      savePngImage "aumentado.png" (ImageRGB8 aumentado)
      putStrLn "Se ha guardado correctamente la imagen"
      let disminuido = cambiarBrillo 0.5 img
      savePngImage "disminuido.png" (ImageRGB8 disminuido)
      putStrLn "Se ha guardado correctamente la imagen"

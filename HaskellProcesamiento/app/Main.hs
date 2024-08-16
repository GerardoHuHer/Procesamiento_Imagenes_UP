module Main where
import Codec.Picture

-- Función que recibe el path de la imagen y devuelve su negativo
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

-- Función para pasar a escala de grises una imagen
blancoNegro :: FilePath -> IO ()
blancoNegro path = do
    -- Leer la imagen desde el archivo
    eImg <- readImage path
    case eImg of
        Left err -> putStrLn $ "Error: " ++ err
        Right dynImg -> do
            let img = convertRGB8 dynImg
            let blancoNegroImg = pixelMap (\(PixelRGB8 r g b) -> let gray = round (fromIntegral (r + g + b) / 3) in PixelRGB8 gray gray gray) img
            savePngImage "blancoNegro.png" (ImageRGB8 blancoNegroImg)
            putStrLn "Imagen en blanco y negro guardada como blancoNegro.png"

main :: IO ()
main = do
    imagenNegativo "/home/gd_15/Descargas/obsidian.png"
    blancoNegro "/home/gd_15/Descargas/obsidian.png"

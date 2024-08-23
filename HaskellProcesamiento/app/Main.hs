module Main where

import Codec.Picture
import Ejemplos
import Tareas

main :: IO ()
main = do
  imagenNegativo "/home/gd_15/Descargas/colores.jpg"
  blancoNegro "/home/gd_15/Descargas/colores.jpg"
  randomColor "/home/gd_15/Descargas/colores.jpg" 8

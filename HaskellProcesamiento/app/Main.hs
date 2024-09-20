module Main where

import Segmentacion
import TareaIluminacion

main :: IO ()
main = do
  -- imagenNegativo "/home/gd_15/Descargas/colores.jpg"
  -- blancoNegro "/home/gd_15/Descargas/colores.jpg"
  -- randomColor "/home/gd_15/Descargas/colores.jpg" 
  -- segmentacion "/home/gd_15/Descargas/colores.jpg"
  runTareaIluminacion "/home/gd_15/Descargas/colores.jpg"

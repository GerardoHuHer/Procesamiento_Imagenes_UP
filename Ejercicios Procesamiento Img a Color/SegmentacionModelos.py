# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:48:10 2024

@author: Eduardo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en color
imagen = cv2.imread("D:\\Procesamiento_Imagenes_UP\\arbol.jpg")

# Convertir la imagen de BGR (OpenCV) a HSV (que es una representación del modelo HSI)
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir el rango de color para segmentar (por ejemplo, detectar un objeto de color rojo)
#rango_bajo = np.array([0, 120, 70])
#rango_alto = np.array([72, 255, 255])



rango_bajo = np.array([0, 64, 90])
rango_alto = np.array([60, 255, 255])


#Azules
#rango_bajo = np.array([60, 64, 90])
#rango_alto = np.array([120, 255, 255])

# Crear una máscara basada en el rango de color
mascara = cv2.inRange(imagen_hsv, rango_bajo, rango_alto)

# Aplicar la máscara a la imagen original
resultado = cv2.bitwise_and(imagen, imagen, mask=mascara)

# Mostrar la imagen original y la imagen segmentada
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title('Imagen Segmentada (Rojo)')
plt.show()

'''
A. Utilizar un algoritmo de suavizado de imágenes y aplicarlo a una imagen en escala de grises.
B. Utilizar un algoritmo de filtrado de detección de bordes y aplicarlo a una imagen en escala de grises.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

def suavizado(path: str) :
    '''
        Función para generar el suavizado de una imagen en este caso con una máscara de 5 x 5
    '''
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    suavizado = np.ones((5,5), np.float32) / 25
    img_s = cv2.filter2D(img, -1, suavizado)
    return (img, img_s)

def bordes(path: str):
    
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    bordes = np.array([[1,2,1], [0,0,0], [-1, -2, -1]])
    img_b = cv2.filter2D(img, -1, bordes)
    return (img, img_b)


path: str = ".\\arbol.jpg"
img, imagen_suavizada = suavizado(path)
img, imagen_bordes = bordes(path)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Imagen Original")

plt.subplot(1, 3, 2)
plt.imshow(imagen_suavizada, cmap="gray")
plt.title("Imagen Suavizada")

plt.subplot(1, 3, 3)
plt.imshow(imagen_bordes, cmap="gray")
plt.title("Bordes de la Imagen")

plt.show()
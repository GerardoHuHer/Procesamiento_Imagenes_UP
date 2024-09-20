import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread(
    "/home/gd_15/Escritorio/Procesamiento_Imagenes_UP/TareaEjercicioIluminación/colores.jpg", cv2.IMREAD_GRAYSCALE)

negativo = 255 - imagen

c = 255 / np.log(1 + np.max(imagen))
logaritmica = c * np.log(1 + imagen)

gamma = 0.5
gamma_correccion = np.array(255 * (imagen / 255) ** gamma, dtype="uint8")

imagenes = [imagen, negativo, logaritmica, gamma_correccion]
titulos = ["Original", "Negativo", "Logarítmica", "Gamma"]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(imagenes[i], cmap="gray")
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

plt.show()

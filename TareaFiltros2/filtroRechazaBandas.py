import cv2 
import numpy as np
import matplotlib.pyplot as plt

def fourier_rechaza_banda(path: str, radio_externo: int = 60, radio_interno: int = 20):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    h, w = img.shape
    c_x, c_y = h // 2, w//2

    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)

    filtro_rechaza_bandas = np.ones((h, w))
    cv2.circle(filtro_rechaza_bandas, (c_x, c_y), radio_externo, 0, -1)
    cv2.circle(filtro_rechaza_bandas, (c_x, c_y), radio_interno, 1, -1)

    f_shift_filtrado = f_shift * filtro_rechaza_bandas

    f_inv_shift = np.fft.ifftshift(f_shift_filtrado)
    imagen_rechaza_bandas = np.abs(np.fft.ifft2(f_inv_shift))

    return img, imagen_rechaza_bandas


path = "D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg"
img, imagen_rechaza_bandas = fourier_rechaza_banda(path)

plt.subplot(1,2,1)
plt.title("Imagen Original")
plt.imshow(img, cmap="gray")

plt.subplot(1,2,2)
plt.title("Imagen Filtro Rechaza-Bandas")
plt.imshow(imagen_rechaza_bandas, cmap="gray")

plt.show()
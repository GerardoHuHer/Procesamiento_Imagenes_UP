import cv2 
import numpy as np
import matplotlib.pyplot as plt

def fourier_pasa_bandas(path: str, radio_externo: int = 60, radio_interno: int = 20):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    h, w = img.shape
    c_x, c_y = h // 2, w//2

    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)

    filtro_pasa_bandas = np.zeros((h, w))
    cv2.circle(filtro_pasa_bandas, (c_x, c_y), radio_externo, 1, -1)
    cv2.circle(filtro_pasa_bandas, (c_x, c_y), radio_interno, 0, -1)

    f_shift_filtrado = f_shift * filtro_pasa_bandas

    f_inv_shift = np.fft.ifftshift(f_shift_filtrado)
    imagen_pasa_bandas = np.abs(np.fft.ifft2(f_inv_shift))

    return img, imagen_pasa_bandas


path = "D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg"
img, imagen_pasa_bandas = fourier_pasa_bandas(path)

plt.subplot(1,2,1)
plt.title("Imagen Original")
plt.imshow(img, cmap="gray")

plt.subplot(1,2,2)
plt.title("Imagen Filtro Pasa-Bandas")
plt.imshow(imagen_pasa_bandas, cmap="gray")

plt.show()
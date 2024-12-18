import cv2  
import numpy as np
import matplotlib.pyplot as plt

def fourier_pasa_bajas(path: str, tam: int):
    # Leemos imagen
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # Calculamos alto y ancho
    
    h, w = img.shape
    # Obtenemos el centro de la imagen con una división entera
    c_x, c_y  = h // 2, w // 2
    # Tamaño del filtro a aplicar, puede ser variable
    radio = tam
    
    # Calculamos la transformada de Fourier
    f = np.fft.fft2(img)
    # TODO Desplazar el cero de frecuencia al centro
    f_shift = np.fft.fftshift(f)

    # Creamos el filtro pasa altas
    # Creamos una matriz de 1's con las dimensiones de la imagen original
    filtro_pasa_bajas = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    cv2.circle(filtro_pasa_bajas, (c_x, c_y), radio, 1, -1)

    # Aplicamos el filtro pasa-altas 
    f_shift_filtrado = f_shift * filtro_pasa_bajas

    # Transformada inversa para obtner la imagen filtrada
    f_inv_shift = np.fft.ifftshift(f_shift_filtrado)
    imagen_pasa_bajas = np.abs(np.fft.ifft2(f_inv_shift))


    return img, imagen_pasa_bajas

path = "D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg"
# path = "/home/gd_15/Escritorio/Procesamiento_Imagenes_UP/arbol.jpg"
img, imagen_pasa_bajas = fourier_pasa_bajas(path, 50)


plt.subplot(1,2,1)
plt.title("Imagen Original")
plt.imshow(img, cmap="gray")

plt.subplot(1,2,2)
plt.title("Imagen con Filtro Pasa-Bajas")
plt.imshow(imagen_pasa_bajas, cmap="gray")

plt.show()

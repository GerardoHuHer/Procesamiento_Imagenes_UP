


import cv2
import matplotlib.pyplot as plt
imagen = cv2.imread("D:\\Procesamiento_Imagenes_UP\\arbol.jpg")


# Convertir una imagen de BGR (usado por OpenCV) a HSI (HSV en OpenCV)
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Separar los canales H, S, V
H, S, V = cv2.split(imagen_hsv)

# Mostrar los tres componentes de HSI
plt.figure(figsize=(10,5))
plt.subplot(1, 3, 1)
plt.imshow(H, cmap='hsv')
plt.title('Tonalidad (Hue)')

plt.subplot(1, 3, 2)
plt.imshow(S, cmap='gray')
plt.title('Saturación (Saturation)')

plt.subplot(1, 3, 3)
plt.imshow(V, cmap='gray')
plt.title('Intensidad (Value)')
plt.show()

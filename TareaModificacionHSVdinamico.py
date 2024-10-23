import cv2
import numpy as np

# Cargar la imagen en color
path = "D:\\Procesamiento_Imagenes_UP\\arbol.jpg"
imagen = cv2.imread(path)

# Convertir la imagen de BGR a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Variables para almacenar los cambios en HSV
tonalidad = 0
saturacion = 0
intensidad = 0

# Tamaño y posición del botón de guardar
boton_pos = (20, 20)  # Coordenadas del botón dentro del área de control (debajo de la imagen)
boton_size = (150, 50)

# Altura extra para incluir el botón debajo de la imagen
altura_extra = 100

# Función para dibujar un botón en la imagen
def dibujar_boton(area_control, texto):
    cv2.rectangle(area_control, boton_pos, (boton_pos[0] + boton_size[0], boton_pos[1] + boton_size[1]), (0, 255, 0), -1)
    cv2.putText(area_control, texto, (boton_pos[0] + 10, boton_pos[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# Función para detectar si el clic está dentro del botón
def clic_en_boton(x, y):
    # Ajustar la posición del clic para que sea dentro del área de control (debajo de la imagen)
    y -= imagen.shape[0]
    if 0 <= y <= boton_size[1] and boton_pos[0] <= x <= boton_pos[0] + boton_size[0]:
        return True
    return False

# Función para actualizar y mostrar la imagen con los cambios en HSV
def actualizar_imagen():
    nueva_hsv = imagen_hsv.copy()
    nueva_hsv[:, :, 0] = (nueva_hsv[:, :, 0] + tonalidad) % 180  # Modificar tonalidad
    nueva_hsv[:, :, 1] = np.clip(nueva_hsv[:, :, 1] + saturacion, 0, 255)  # Modificar saturación
    nueva_hsv[:, :, 2] = np.clip(nueva_hsv[:, :, 2] + intensidad, 0, 255)  # Modificar intensidad
    return cv2.cvtColor(nueva_hsv, cv2.COLOR_HSV2BGR)

# Callback de evento de clic de ratón
def callback_clic(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Comprobar si el clic está dentro del botón en el área de control
        if y > imagen.shape[0] and clic_en_boton(x, y):
            imagen_guardada = actualizar_imagen()
            cv2.imwrite("modificacionHSV.jpg", imagen_guardada)  # Guardar la imagen
            print("Imagen guardada como 'modificacionHSV.jpg'.")

# Crear las funciones de trackbar para modificar HSV
def cambiar_tonalidad(x):
    global tonalidad
    tonalidad = x

def cambiar_saturacion(x):
    global saturacion
    saturacion = x

def cambiar_intensidad(x):
    global intensidad
    intensidad = x

# Crear una ventana y los trackbars
cv2.namedWindow('Modificación HSV')
cv2.setMouseCallback('Modificación HSV', callback_clic)
cv2.createTrackbar('Tonalidad', 'Modificación HSV', 0, 179, cambiar_tonalidad)
cv2.createTrackbar('Saturación', 'Modificación HSV', 0, 255, cambiar_saturacion)
cv2.createTrackbar('Intensidad', 'Modificación HSV', 0, 255, cambiar_intensidad)

# Bucle principal
while True:
    # Crear una copia de la imagen con los cambios
    imagen_modificada = actualizar_imagen()

    # Crear un área extendida para agregar la zona del botón (debajo de la imagen)
    area_extendida = np.zeros((imagen.shape[0] + altura_extra, imagen.shape[1], 3), dtype=np.uint8)
    
    # Colocar la imagen modificada en la parte superior del área extendida
    area_extendida[:imagen.shape[0], :, :] = imagen_modificada
    
    # Dibujar el botón en el área de control (debajo de la imagen)
    dibujar_boton(area_extendida[imagen.shape[0]:, :, :], "Guardar")

    # Mostrar la imagen con el botón en la ventana
    cv2.imshow('Modificación HSV', area_extendida)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

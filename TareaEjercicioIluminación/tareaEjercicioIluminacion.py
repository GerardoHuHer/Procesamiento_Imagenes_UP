
from PIL import Image
import matplotlib.pyplot as plt


def cambiar_brillo(img, factor: int):
    imagen_aux = img.copy()
    mapaBit = list(img.getdata())
    mapaBit = list(map(lambda pixel: (
        min(255, max(0, int(pixel[0] * factor))),
        min(255, max(0, int(pixel[1] * factor))),
        min(255, max(0, int(pixel[2] * factor)))
    ), mapaBit))
    imagen_aux.putdata(mapaBit)
    return imagen_aux


img = Image.open("./colores.jpg")

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("Imagen Original")
plt.imshow(img)

aumentado = cambiar_brillo(img, 1.5)
aumentado.save("aumentado.jpg")
plt.subplot(1, 3, 2)
plt.title("Brillo aumentado")
plt.imshow(aumentado)

img_brillo_disminuido = cambiar_brillo(img, 0.5)
img_brillo_disminuido.save("disminuido.jpg")
plt.subplot(1, 3, 3)
plt.title("Brillo disminuido")
plt.imshow(img_brillo_disminuido)

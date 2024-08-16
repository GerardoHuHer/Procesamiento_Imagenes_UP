'''
    Tarea 1: Generar un código que dada una imagen a color nos devuelva su negativo
'''
from PIL import Image

def imagenNegativo(path: str):
    '''
        Función que recibe el path de la imagen y devuelve su negativo
    '''
    img = Image.open(path)
    img.show()
    img2 = img.copy()
    pixels = list(img2.getdata())
    negativo = list(map(lambda pixel: (255 - pixel[0], 255 - pixel[1], 255 - pixel[2]), pixels))
    img2.putdata(negativo)
    img2.show()

def blancoNegro(path: str):
    '''
        Función para pasar a escala de grises una imagen
    '''
    img = Image.open(path)
    img.show()
    img2 = img.copy()
    img2 = img2.convert("L")
    pixels = list(img2.getdata())
    grises = list(map(lambda pixel: (255 - pixel), pixels))
    img2.putdata(grises)
    img2.show()

imagenNegativo("/home/gd_15/Descargas/obsidian.png")
blancoNegro("/home/gd_15/Descargas/obsidian.png")



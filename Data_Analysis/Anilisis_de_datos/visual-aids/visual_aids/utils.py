"""Funciones útiles para crear ayudas visuales."""

from PIL import Image
import matplotlib.pyplot as plt


def make_grayscale(filepath, save=False):
    """Convierte un archivo de imagen a escala de grises y, opcionalmente, lo guarda en `save`"""
    img = Image.open(filepath).convert('LA')
    if save:
        img.save(save)
    return img


def edit_image(filepath, replacements, save=False):
    """
    Reemplaza los colores de la imagen especificada píxel a píxel.

    Parámetros:
        - filepath: La ruta a la imagen
        - reemplazos: Un diccionario cuyas claves son
                        tuplas de color RGBA a reemplazar y
                        los valores son las sustituciones
        - guardar: Si desea guardar el archivo de nuevo a la ruta de archivo.

    Devuelve:
        Imagen modificada.

    Ejemplo de uso:
        edit_image('netflix_after_hours_trading.png', {(179, 0, 0, 255): (255, 0, 0, 255)})
    """
    im = Image.open(filepath)

    modified_pixels = [
        replacements.get(color, color) for color in im.getdata()
    ]

    modified_im = Image.new(im.mode, im.size)
    modified_im.putdata(modified_pixels)

    if save:
        modified_im.save(filepath)

    return modified_im

def save_plot(file):
    """Guardar la cifra actual."""
    plt.savefig(file, dpi=300, bbox_inches='tight')

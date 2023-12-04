"""Funciones de utilidad para trabajar con colores."""

import re

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


def hex_to_rgb_color_list(colors):
    """
    Toma un color o una lista de colores en código hexadecimal y los convierte
    a colores RGB en el rango [0,1].

    Parámetros:
        - Colores: Color o lista de cadenas de color del formato
                  #FFF' o '#FFFFFF'.

    Devuelve:
        El color o lista de colores en representación RGB.
    """
    if isinstance(colors, str):
        colors = [colors]

    for i, color in enumerate(
        [color.replace('#', '') for color in colors]
    ):
        hex_length = len(color)

        if hex_length not in [3, 6]:
            raise ValueError(
                'Colors must be of the form #FFFFFF or #FFF'
            )

        regex = '.' * (hex_length // 3)
        colors[i] = [
            int(val * (6 // hex_length), 16) / 255
            for val in re.findall(regex, color)
        ]

    return colors[0] if len(colors) == 1 else colors


def blended_cmap(rgb_color_list):
    """
    Creado un mapa de color que mezcla de un color a otro.

    Parámetros:
        - rgb_color_list: Una lista de colores representados como [R, G, B]
          en el rango [0, 1], como [[0, 0, 0], [1, 1, 1]
          para el blanco y el negro, respectivamente.

    Devuelve:
        Un objeto matplotlib `ListedColormap`.
    """
    if not isinstance(rgb_color_list, list):
        raise ValueError('Los colores deben pasarse como una lista.')
    elif len(rgb_color_list) < 2:
        raise ValueError('Debe especificar al menos 2 colores.')
    elif (
        not isinstance(rgb_color_list[0], list)
        or not isinstance(rgb_color_list[1], list)
    ) or (
        len(rgb_color_list[0]) != 3 or len(rgb_color_list[1]) != 3
    ):
        raise ValueError(
            'Cada color debe representarse como una lista de tamaño 3.'
        )

    N, entries = 256, 4 # rojo, verde, azul, alfa
    rgbas = np.ones((N, entries))

    segment_count = len(rgb_color_list) - 1
    segment_size = N // segment_count
    remainder = N % segment_count # necesito añadir esto más tarde

    for i in range(entries - 1): # nosotros no alteramos alfas
        updates = []
        for seg in range(1, segment_count + 1):
            # determinar cuánto hay que añadir para tener en cuenta los remanentes
            offset = 0 if not remainder or seg > 1 else remainder

            updates.append(np.linspace(
                start=rgb_color_list[seg - 1][i],
                stop=rgb_color_list[seg][i],
                num=segment_size + offset
            ))

        rgbas[:,i] = np.concatenate(updates)

    return ListedColormap(rgbas)


def draw_cmap(cmap, values=np.array([[0, 1]]), **kwargs):
    """
    Dibuja una barra de colores para visualizar un mapa de colores.

    Parámetros:
        - cmap: Un mapa de colores matplotlib
        - valores: Los valores a utilizar para el colormap, por defecto [0, 1]
        - kwargs: Argumentos de palabra clave para pasar a `plt.colorbar()`.

    Devuelve:
        Un objeto matplotlib `Colorbar`, que puede guardar con:
        `plt.savefig(<nombre_archivo>, bbox_inches='tight')`
    """
    img = plt.imshow(values, cmap=cmap)
    cbar = plt.colorbar(**kwargs)
    img.axes.remove()
    return cbar
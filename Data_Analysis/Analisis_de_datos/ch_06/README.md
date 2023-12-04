# Capítulo 6: Trazado con Seaborn y técnicas de personalización

Este capítulo continúa la discusión sobre la visualización de datos enseñándote a usar la librería `seaborn` para visualizar tus datos de forma larga y dándote las herramientas que necesitas para personalizar tus visualizaciones, haciéndolas listas para la presentación.

## Contenido

Hay tres NoteBook en los que trabajaremos, cada uno numerado de acuerdo a cuando serán usados:

- [`1-introduccion_a_seaborn.ipynb`](./1-introduccion_a_seaborn.ipynb): te introduce al trazado con `seaborn`.
- [`2-formateando_plots.ipynb`](./2-formateando_plots.ipynb): cubre el formateo y etiquetado de gráficos.
- [`3-customizando_visualizaciones.ipynb`](./3-customizando_visualizaciones.ipynb): proporciona información sobre personalización de gráficos, incluyendo líneas de referencia, anotaciones y mapas de colores personalizados.

-----

También hay un cuaderno **bonus** que recorre un ejemplo de trazado de datos en un mapa utilizando casos COVID-19 en todo el mundo: [`covid19.ipynb`](./covid19.ipynb). Puede utilizarse para iniciarse en el uso de mapas en Python y también se basa en algunos de los formatos tratados en el capítulo.

-----

Además, tenemos dos módulos de Python que contienen funciones que utilizaremos en los cuadernos mencionados:

- [`color_utils.py`](./color_utils.py): incluye varias funciones para trabajar con colores en Python.
- [`viz.py`](./viz.py): contiene una función para generar gráficos de regresión y residuos para cada par de variables del conjunto de datos usando `seaborn` y otra función para generar un KDE con líneas de referencia para 1, 2 y 3 desviaciones estándar de la media.

Todos los conjuntos de datos necesarios para los cuadernos mencionados, junto con la información sobre ellos, pueden encontrarse en el directorio [`data/`](./data).
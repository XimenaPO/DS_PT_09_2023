# Capítulo 4: Agregación de Pandas DataFrames

Este capítulo le enseña cómo consultar y combinar objetos `DataFrame`, realizar operaciones complejas sobre ellos, incluyendo cálculos de balanceo y agregaciones, y cómo trabajar eficazmente con datos de series temporales.

## Contenido

Hay cuatro cuadernos en los que trabajaremos, cada uno numerado según el momento en que se utilizarán:

- [`1-consulta_y_merge.ipynb`](./1-consulta_y_merge.ipynb): muestra cómo consultar y combinar objetos `DataFrame
- [`2-operaciones_con_dataframe.ipynb`](./2-operaciones_con_dataframe.ipynb): muestra una variedad de operaciones de enriquecimiento de datos, como el binning y el cálculo de ventanas, y cómo realizarlas eficientemente con los métodos `apply()` y `pipe()`.
- [3-agregaciones.ipynb`](./3-agregaciones.ipynb): discute cómo realizar agregaciones en los datos, incluyendo tablas dinámicas, tabulaciones cruzadas y cálculos basados en la pertenencia a grupos con el método `groupby()`.
- [`4-time_series.ipynb`](./4-time_series.ipynb): ilustra cómo trabajar eficazmente con series temporales

-----

También hay un cuaderno **bonus** que utiliza widgets interactivos para que entiendas mejor los cálculos de ventanas: [`calculo_de_ventana.ipynb`](./calculo_de_ventana.ipynb).

-----

Además de los cuadernos mencionados, tenemos dos archivos adicionales:
- [`0-weather_data_collection.ipynb`](./0-weather_data_collection.ipynb): (opcional) contiene el código utilizado para recoger los datos meteorológicos utilizados en el capítulo
- [`window_calc.py`](./window_calc.py): contiene una función que utiliza tuberías para realizar diversos cálculos de ventanas

Todos los conjuntos de datos necesarios para los cuadernos mencionados, junto con la información sobre los mismos, se encuentran en el directorio [`data/`](./data). Los ejercicios de final de capítulo utilizarán los conjuntos de datos del directorio [`exercises/`](./exercises); las soluciones a estos ejercicios se encuentran en el directorio [`solutions/ch_04/`](../solutions/ch_04) del repositorio.


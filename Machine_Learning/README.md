# Bootcamp de Data Science y Machine Learning

_Autor: Juan Maniglia_

## Descripción:

Este repositorio contiene materiales, ejercicios y recursos para el bootcamp de Data Science y Machine Learning en Python. El contenido está enfocado en cuatro áreas principales: aprendizaje supervisado, aprendizaje no supervisado, series temporales y deep learning. El bootcamp se basa en las bibliotecas de Python `scikit-learn`, `TensorFlow` y `PyTorch`.

## Contenido

1. **Aprendizaje supervisado**: se exploran diferentes modelos y técnicas para predecir variables objetivo a partir de conjuntos de datos etiquetados.
    - Regresión lineal
    - Regresión logística
    - Máquinas de soporte vectorial (SVM)
    - Árboles de decisión
    - Random Forest
    - Boosting

2. **Aprendizaje no supervisado**: se estudian técnicas para encontrar patrones y estructuras en conjuntos de datos sin etiquetar.
    - Clustering (K-means, DBSCAN)
    - Reducción de dimensionalidad (PCA)

3. **Series temporales**: se presentan modelos y técnicas para analizar y predecir datos a lo largo del tiempo.
    - Descomposición de series temporales
    - Modelos autorregresivos (AR, ARIMA)
    - Modelos de suavizado exponencial

4. **Deep Learning**: se exploran arquitecturas de redes neuronales y sus aplicaciones en diferentes dominios.
    - Redes neuronales convolucionales (CNN) para imágenes
    - Redes neuronales recurrentes (RNN) para secuencias
    - Modelos generativos (GAN, VAE)

## Requisitos

Es necesario tener instalado Python 3.6 o superior y las siguientes bibliotecas:

- `numpy`
- `pandas`
- `scikit-learn`
- `tensorflow`
- `pytorch`
- `matplotlib`
- `seaborn`
- `statsmodels`

## Instalación

Para instalar las dependencias necesarias, ejecute el siguiente comando:

> pip install -r requirements.txt


## Cómo contribuir

Si deseas contribuir al repositorio, por favor realiza un _fork_ del mismo y crea una _pull request_ con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulte el archivo [LICENSE](LICENSE).


## Actualizar el fork a partir del repositorio original

1. Agregar el repositorio original como "upstream":

> git remote add upstream https://github.com/JuanManiglia/Machine_Learning.git


2. Obtener los cambios del repositorio original:

> git fetch upstream


3. Cambiar a la rama principal de tu fork (si no estás ya en ella):

> git checkout main


4. Combinar los cambios del repositorio original a tu rama principal:

> git merge upstream/main


5. Si es necesario, resuelve cualquier conflicto y realiza un commit con los cambios.

6. Empuja los cambios a tu fork en GitHub:

> git push

Con estos pasos, tu fork estará actualizado con los últimos cambios del repositorio original.

![Fork de GitHub](https://miro.medium.com/v2/resize:fit:1400/1*qOtT_fhdwzty5T_AylY8YQ.png)

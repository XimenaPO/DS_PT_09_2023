# ESTADISTICA

## Prueba de hipótesis: 
Establece una hipótesis nula y una hipótesis alternativa y utiliza la evidencia de los datos para evaluar si se puede rechazar o no la hipótesis nula.
- ### 1. Prueba t de Student: 
Compara las medias de dos grupos independientes.
- ### 2. Prueba t pareada: 
Compara las medias de dos grupos relacionados o pareados.
- ### 3. Prueba de chi-cuadrado: 
Evalúa la asociación entre variables categóricas.
- ### 4. Prueba F: 
Compara la varianza de dos o más poblaciones.

## Intervalos de confianza: 
Estima un rango en el que es probable que se encuentre un parámetro poblacional, basándose en la información de una muestra.

## Regresión: 
Modela la relación entre una variable dependiente y una o más variables independientes.
- ### 1. Regresión lineal simple: 
Modela la relación entre una variable dependiente y una variable independiente.
- ### 2. Regresión lineal múltiple: 
Modela la relación entre una variable dependiente y varias variables independientes.
- ### 3. Regresión logística: 
Modela la probabilidad de una variable categórica en función de una o más variables independientes.

## Análisis de varianza (ANOVA): 
Compara las medias de tres o más grupos y determina si existe una diferencia significativa entre ellos.
- ### 1. ANOVA de un factor: 
Compara las medias de los grupos basándose en un solo factor o variable independiente.
- ### 2. ANOVA de dos factores: 
Compara las medias de los grupos basándose en dos factores o variables independientes.
- ### 3. Análisis de covarianza (ANCOVA): 
Similar al ANOVA, pero también considera una o más variables de covariables que pueden afectar la variable dependiente.

## Análisis de componentes principales (PCA): 
Reduce la dimensionalidad de un conjunto de datos al proyectarlos en un espacio con menos dimensiones, manteniendo la mayor cantidad de variación posible.

## Análisis de correlación: 
Mide la fuerza y dirección de la relación lineal entre dos variables.

- ### 1. Coeficiente de correlación de Pearson

- ### 2. Coeficiente de correlación de Spearman

- ### 3. Coeficiente de correlación de Kendall

## Los tests de normalidad:

son pruebas estadísticas que se utilizan para determinar si una muestra de datos se ajusta a una distribución normal (también conocida como distribución gaussiana). Estas pruebas son importantes porque muchas técnicas estadísticas asumen que los datos siguen una distribución normal, y si esta suposición no se cumple, los resultados pueden ser incorrectos o no válidos.

Los tests de normalidad más comunes y cuándo se utilizan:

### Prueba de Shapiro-Wilk: 
Es una prueba ampliamente utilizada para comprobar la normalidad de una muestra. Es especialmente adecuada para muestras pequeñas (menos de 50 observaciones), ya que es más sensible a las desviaciones de la normalidad en este tipo de muestras.
### Prueba de Kolmogorov-Smirnov: 
Esta prueba compara la función de distribución acumulativa (FDA) de la muestra con la función de distribución acumulativa teórica de una distribución normal. Es más adecuada para muestras más grandes, pero tiende a ser menos sensible a las desviaciones de la normalidad en comparación con la prueba de Shapiro-Wilk
### Prueba de Lilliefors: 
Es una variante de la prueba de Kolmogorov-Smirnov diseñada específicamente para muestras pequeñas cuando los parámetros de la distribución normal (media y varianza) son desconocidos y se estiman a partir de los datos.
### Prueba de Anderson-Darling: 
Es otra prueba que compara la función de distribución acumulativa de la muestra con la función de distribución acumulativa teórica de una distribución normal. La prueba de Anderson-Darling da más peso a las colas de la distribución, lo que la hace más sensible a las desviaciones de la normalidad en las colas.
### Prueba de D'Agostino-Pearson: 
Esta prueba se basa en los coeficientes de asimetría (skewness) y curtosis de la muestra para evaluar la normalidad. Es más adecuada para muestras medianas y grandes.
### Prueba de Jarque-Bera: 
Es otra prueba basada en la asimetría y curtosis de la muestra y es especialmente útil para muestras grandes.

La elección de la prueba de normalidad adecuada depende del tamaño de la muestra y de las características específicas de los datos en estudio. En general, se recomienda utilizar la prueba de Shapiro-Wilk para muestras pequeñas y una combinación de pruebas, como la prueba de Kolmogorov-Smirnov, Anderson-Darling y D'Agostino-Pearson, para muestras medianas y grandes.

## Los tests de correlación:

son pruebas estadísticas que se utilizan para medir la fuerza y dirección de la relación lineal entre dos variables. Estas pruebas son útiles para identificar si existe una asociación entre las variables y para evaluar la naturaleza de esa asociación.

Los tests de correlación más comunes y cuándo se utilizan:

### Coeficiente de correlación de Pearson (r de Pearson): 
Es el test de correlación más utilizado y mide la relación lineal entre dos variables continuas. La correlación de Pearson es apropiada cuando ambas variables siguen una distribución normal y la relación entre ellas es lineal. El coeficiente varía entre -1 y 1, donde -1 indica una correlación negativa perfecta, 1 indica una correlación positiva perfecta y 0 indica que no hay correlación.
### Coeficiente de correlación de Spearman (rho de Spearman): 
Es una medida de correlación no paramétrica que evalúa la relación monótona entre dos variables. No requiere que los datos sigan una distribución normal y es menos sensible a la presencia de valores extremos que la correlación de Pearson. Es apropiado cuando al menos una de las variables es ordinal (categórica con un orden) o cuando la relación entre las variables no es lineal pero sí monótona.
### Coeficiente de correlación de Kendall (tau de Kendall): 
También es una medida de correlación no paramétrica que evalúa la relación monótona entre dos variables. Es similar al coeficiente de correlación de Spearman, pero es especialmente útil en situaciones en las que hay empates en los datos (observaciones con valores idénticos) o cuando se trabaja con muestras pequeñas.

La elección del test de correlación adecuado depende de la naturaleza de las variables y de la relación que se espera encontrar entre ellas. Se recomienda utilizar el coeficiente de correlación de Pearson para variables continuas con una relación lineal y una distribución normal, mientras que se aconseja utilizar el coeficiente de correlación de Spearman o de Kendall cuando se trabaja con variables ordinales o con relaciones no lineales.

## Los tests de hipótesis paramétricos:
Son pruebas estadísticas que se basan en supuestos específicos sobre la distribución de los datos y los parámetros poblacionales. Estos tests se utilizan para comparar medias, proporciones, varianzas y otras características de una o más poblaciones.

Los tests de hipótesis paramétricos más comunes y cuándo se utilizan:

### Prueba t de Student (t-test): 
Compara las medias de dos grupos independientes. Se utiliza cuando se tiene una variable categórica con dos niveles (por ejemplo, hombres y mujeres) y una variable continua (por ejemplo, ingresos), y se desea evaluar si hay una diferencia significativa en las medias de la variable continua entre los dos grupos.
### Prueba t pareada (paired t-test): 
Compara las medias de dos grupos relacionados o pareados, como las mediciones antes y después de un tratamiento en el mismo grupo de sujetos. Se utiliza cuando se tiene un diseño experimental de medidas repetidas o pareadas y se desea evaluar si hay una diferencia significativa en las medias antes y después del tratamiento.
### Prueba F (F-test) o ANOVA (Análisis de varianza): 
Compara las medias de tres o más grupos y determina si existe una diferencia significativa entre ellos. Se utiliza cuando se tiene una variable categórica con tres o más niveles y una variable continua, y se desea evaluar si hay diferencias significativas en las medias de la variable continua entre los diferentes niveles de la variable categórica.
### Prueba de proporciones z (z-test for proportions): 
Compara las proporciones de dos grupos independientes. Se utiliza cuando se tiene una variable categórica con dos niveles y se desea evaluar si hay una diferencia significativa en las proporciones entre los dos grupos.
### Prueba chi-cuadrado de independencia: 
Evalúa la asociación entre dos variables categóricas. Se utiliza cuando se desea determinar si hay una relación entre dos variables categóricas en una muestra.
### Regresión lineal: 
Modela la relación entre una variable dependiente y una o más variables independientes. Se utiliza cuando se desea explorar la relación entre una variable continua y una o más variables independientes (continuas o categóricas) y predecir la variable dependiente a partir de las variables independientes.

Los tests de hipótesis paramétricos se utilizan cuando se cumplen ciertos supuestos, como la normalidad de los datos, la homogeneidad de las varianzas y la independencia de las observaciones. Si estos supuestos no se cumplen, es posible que sea necesario utilizar pruebas no paramétricas, que son más flexibles y no requieren supuestos específicos sobre la distribución de los datos.

## Los tests de hipótesis no paramétricos:
Son pruebas estadísticas que no hacen supuestos específicos sobre la distribución de los datos ni los parámetros poblacionales. Estos tests son útiles cuando no se cumplen los supuestos requeridos para los tests paramétricos, como la normalidad, la homogeneidad de las varianzas o la independencia de las observaciones.

Los tests de hipótesis no paramétricos más comunes y cuándo se utilizan:

### Prueba de Wilcoxon de rangos con signo (Signed Rank Test): 
Es el equivalente no paramétrico de la prueba t pareada. Se utiliza para comparar las medias de dos grupos relacionados o pareados cuando no se cumplen los supuestos de normalidad.
### Prueba de Mann-Whitney U (Wilcoxon Rank Sum Test): 
Es el equivalente no paramétrico de la prueba t de Student. Se utiliza para comparar las medias de dos grupos independientes cuando no se cumplen los supuestos de normalidad y homogeneidad de las varianzas.
### Prueba de Kruskal-Wallis: 
Es el equivalente no paramétrico del ANOVA de un factor. Se utiliza para comparar las medias de tres o más grupos independientes cuando no se cumplen los supuestos de normalidad y homogeneidad de las varianzas.
### Prueba de Friedman: 
Es el equivalente no paramétrico del ANOVA de medidas repetidas. Se utiliza para comparar las medias de tres o más grupos relacionados o pareados cuando no se cumplen los supuestos de normalidad.
### Coeficiente de correlación de Spearman (rho de Spearman): 
Es una medida de correlación no paramétrica que evalúa la relación monótona entre dos variables. Es apropiado cuando al menos una de las variables es ordinal (categórica con un orden) o cuando la relación entre las variables no es lineal pero sí monótona.
### Coeficiente de correlación de Kendall (tau de Kendall): 
También es una medida de correlación no paramétrica que evalúa la relación monótona entre dos variables. Es similar al coeficiente de correlación de Spearman, pero es especialmente útil en situaciones en las que hay empates en los datos (observaciones con valores idénticos) o cuando se trabaja con muestras pequeñas.
### Prueba de chi-cuadrado de bondad de ajuste: 
Compara la distribución observada de una variable categórica con una distribución teórica esperada. Se utiliza para determinar si los datos observados se ajustan a una distribución específica.
### Prueba de chi-cuadrado de independencia: 
Evalúa la asociación entre dos variables categóricas. Aunque también es una prueba paramétrica, se incluye aquí porque es muy útil en situaciones en las que no se cumplen los supuestos de normalidad y homogeneidad de las varianzas.

Los tests de hipótesis no paramétricos se utilizan cuando los supuestos de los tests paramétricos no se cumplen o cuando se trabaja con datos ordinales o de escala nominal. Aunque son más flexibles que los tests paramétricos, suelen tener menos poder estadístico, lo que significa que pueden ser menos sensibles para detectar diferencias o relaciones significativas.
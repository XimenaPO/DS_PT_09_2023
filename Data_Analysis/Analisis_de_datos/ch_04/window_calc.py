"""Ilustración de tuberías utilizando cálculos de ventanas"""


def window_calc(df, func, agg_dict, *args, **kwargs):
  """
    Ejecuta un cálculo de ventana de su elección en un objeto `DataFrame`.
    
    Parámetros:
        - df: El objeto `DataFrame` sobre el que ejecutar el cálculo.
        - func: El método de cálculo de la ventana que toma `df`
          como primer argumento.
        - agg_dict: Información a pasar a `agg()`, puede ser un
          diccionario que asigna las columnas a la función
          a usar, un nombre de cadena para la función,
          o la propia función.
        - args: Argumentos posicionales para pasar a `func`.
        - kwargs: Argumentos de palabra clave para pasar a `func`.
    
    Devuelve:
        Un nuevo objeto `DataFrame`.
    """
  return df.pipe(func, *args, **kwargs).agg(agg_dict)
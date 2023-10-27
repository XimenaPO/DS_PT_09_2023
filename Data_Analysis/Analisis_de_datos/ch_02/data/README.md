# Acerca de los datos

| Fichero | Descripción | Fuente
| --- | --- | --- |
| `earthquakes.csv` | Datos de terremotos desde el 18 de septiembre de 2018 hasta el 13 de octubre de 2018. | API de terremotos del Servicio Geológico de Estados Unidos (USGS). |
| `example_data.csv` | Cinco filas de `earthquakes.csv` que contienen un subconjunto de las columnas. | API de terremotos del US Geological Survey (USGS). |
| `parsed.csv` | Datos de `earthquakes.csv` con una columna adicional para la localización (extraída de los datos para manejar múltiples nombres para la misma entidad). | API de terremotos del Servicio Geológico de Estados Unidos (USGS). |
| `quakes.db` | Base de datos SQLite con una única tabla, `tsunamis`, que contiene todos los datos de los terremotos de `earthquakes.csv` acompañados de un tsunami. | API de terremotos del US Geological Survey (USGS). |
| `tsunamis.csv` | Datos de todos los terremotos de `earthquakes.csv` acompañados de tsunami. | API de terremotos del Servicio Geológico de Estados Unidos (USGS). |

### Fuente
Puede encontrar información sobre la API de terremotos del US Geological Survey (USGS) [aquí](https://earthquake.usgs.gov/fdsnws/event/1/). En este capítulo veremos cómo recopilar estos datos.

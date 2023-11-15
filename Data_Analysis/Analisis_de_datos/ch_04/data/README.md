# Acerca de los datos

| Archivo | Descripción | Fuente |
| --- | --- | --- |
| `dirty_data.csv` | Datos meteorológicos sucios de la sección *Manejo de datos duplicados, faltantes o inválidos*. | Adaptado del conjunto de datos GHCND de la API del NCEI |
| `fb_2018.csv` | Precio de apertura, máximo, mínimo y cierre diario de las acciones de Facebook, junto con el volumen negociado en 2018. | El paquete `stock_analysis`. |
| `fb_week_of_may_20_per_minute.csv` | Precio de apertura, máximo, mínimo y cierre por minuto de las acciones de Facebook, junto con el volumen negociado desde el 20 de mayo de 2019 hasta el 24 de mayo de 2019. | Nasdaq |
| `melted_stock_data.csv` | El contenido de `fb_week_of_may_20_per_minute.csv` fundido en una sola columna para el precio y otra para la marca de tiempo. | Adaptado de Nasdaq |
| `nyc_weather_2018.csv` | Datos meteorológicos de formato largo para la ciudad de Nueva York a través de varias estaciones. | El conjunto de datos GHCND de la API del NCEI. |
| `stocks.db` | Las tablas `fb_prices` y `aapl_prices` contienen los precios de las acciones de Facebook y Apple, respectivamente, del 20 de mayo de 2019 al 24 de mayo de 2019. Facebook tiene una granularidad de minutos, mientras que Apple tiene marcas de tiempo que incluyen segundos (ficticios). | Adaptado de Nasdaq |
| `weather_by_station.csv` | Datos meteorológicos de formato largo para la ciudad de Nueva York a través de varias estaciones, junto con información sobre la estación. | El conjunto de datos GHCND de la API del NCEI y el punto final `stations`. |
| `weather_stations.csv` | Información sobre todas las estaciones que proporcionan datos meteorológicos para la ciudad de Nueva York. | El punto final `stations` de la API del NCEI. |
| `weather.db` | La tabla `weather` contiene datos meteorológicos de la ciudad de Nueva York, mientras que la tabla `stations` contiene información sobre las estaciones. | El conjunto de datos GHCND de la API del NCEI y el punto final `stations`. |

### Fuentes
- Los datos del Nasdaq contienen datos bursátiles por minutos y se recopilaron antes de que el Nasdaq actualizara su sitio web. El antiguo sitio se cerrará en breve, pero mientras siga activo, los datos pueden consultarse aquí: [FB](https://old.nasdaq.com/symbol/fb/interactive-chart), [AAPL](https://old.nasdaq.com/symbol/aapl/interactive-chart). Tenga en cuenta que los datos de Apple se recopilaron antes del [desdoblamiento de acciones de agosto de 2020](https://www.marketwatch.com/story/3-things-to-know-about-apples-stock-split-2020-08-28). Encontrará más datos en el nuevo [Nasdaq website](https://www.nasdaq.com/market-activity/stocks). 
- Los Centros Nacionales de Información Medioambiental (NCEI) ofrecen una [API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2), que utilizamos para acceder al conjunto de datos [*Global Historical Climatology Network - Daily* (GHCND)](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/GHCND_documentation.pdf).
- El [`stock_analysis`](https://github.com/stefmolin/stock-analysis) contiene interfaces fáciles de usar para el análisis técnico básico de acciones.
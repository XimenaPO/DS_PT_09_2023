import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

df = sns.load_dataset('tips')

latlog = {'Madrid': {'lat': 40.416775, 'lon': -3.703790},
           'Barcelona': {'lat': 41.385064, 'lon': 2.173404},
           'Valencia': {'lat': 39.469910, 'lon': -0.376288},
           'Sevilla': {'lat': 37.389092, 'lon': -5.984459},
           'Zaragoza': {'lat': 41.648823, 'lon': -0.889085}
           }

city = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Zaragoza']

city_random = np.random.choice(city,244)

df['city'] = city_random
df['lat'] = df['city'].map(latlog).map(lambda x: x['lat'])
df['lon'] = df['city'].map(latlog).map(lambda x: x['lon'])

map_df = df[['lat', 'lon']]
st.map(map_df, zoom=15)
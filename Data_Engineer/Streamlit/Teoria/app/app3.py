import seaborn as sns
import pandas as pd
import streamlit as st

df = sns.load_dataset('penguins')

st.title('Ejemplo de uso de st.write()')

st.write("Hola :sunglasses: :heart:")

st.write(1+1)

a = 2**3
st.write(a*5)

st.write(df.head(5))

st.write('st.write("text", df)', df.head(7))

import streamlit as st
from PIL import Image

image = Image.open(r'C:\Users\jamr1\Documents\Data_Science\GITHUB\DS_PT_09_2023\Data_Engineer\Streamlit\Teoria\img\591e3af95df3c.jpeg')
image2 = Image.open(r'C:\Users\jamr1\Documents\Data_Science\GITHUB\DS_PT_09_2023\Data_Engineer\Streamlit\Teoria\img\images.jpg')

st.image(image)
st.image(image2)
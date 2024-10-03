import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Dashboard Analisis E-Commerce")

data = pd.read_csv("hasil_analisis.csv")

st.write("Produk Terlaris")
fig, ax = plt.subplots()
data['product_id'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

st.write("Jumlah Kuantitas Terjual per Produk")
fig2, ax2 = plt.subplots()
data.groupby('product_id')['quantity'].sum().plot(kind='bar', ax=ax2)
st.pyplot(fig2)

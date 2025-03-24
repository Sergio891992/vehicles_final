import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.title('App gráficas de autos')

build_histogram = st.checkbox('Construir un histograma')
hist_button = st.button('Construir un histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de auncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir una gráfica de dispersión')

if disp_button:
    st.write('Creación de gráfico de dispersión con relación de precio de autos y kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

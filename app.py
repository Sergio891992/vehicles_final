import streamlit as st
import pandas as pd
import plotly as plt
car_data = pd.read_csv(r'C:\Users\Sergio\Desktop\Tripleten\vehicles_final\vehicles_us.csv')

hist_button = st.button('Construir histograma')
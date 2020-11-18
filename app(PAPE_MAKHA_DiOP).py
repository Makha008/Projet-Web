import streamlit as st
# import des librairies classiques
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import dask.dataframe as dd
import csv

st.title("My application")

st.header("Projet Data visualisation")


st.sidebar.header("Python Web")
st.sidebar.text("Pape Makha Diop")
st.sidebar.text("M1 TL")

st.subheader("Affichage des données et commentaire du dataset")
data = pd.read_csv('C:/Users/makha/Documents/Doc/CoursM1/Python/Python Web/TP/malnutrition-estimates.csv')
data = pd.read_csv('C:/Users/makha/Documents/Doc/CoursM1/Python/Python Web/TP/country-wise-average.csv')
data.info()

if st.checkbox("afficher les information du dataset"):
    number = st.number_input("Nombre de lignes à afficher")
    st.dataframe(data.head(int(number)))

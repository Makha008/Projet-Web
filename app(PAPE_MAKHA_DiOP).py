# import des librairies classiques
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import dask.dataframe as dd

#importation du fichiers
data = pd.read_csv('C:/Users/makha/Documents/Doc/CoursM1/Python/Python Web/TP/malnutrition-estimates.csv')
#on supprime les colonnes non utilisés
data.drop(['Unnamed: 0','ISO code','Survey Year','Source','Report Author','Notes','Short Source'], axis=1, inplace=True)

#titre de l'application
st.title("My application")

#l'entete
st.header("Projet Data visualisation")

#nav
st.sidebar.header("Python Web")
st.sidebar.text("Pape Makha Diop")
st.sidebar.text("M1 TL")

#paragraph
st.subheader("Affichage des données et commentaire du dataset")

if st.checkbox("afficher les information du dataset"):
    number = st.number_input("Nombre de lignes à afficher")
    st.dataframe(data.head(int(10)))
    
if st.button("afficher les nom des clonnes"):
    st.write(data.columns.tolist())
    
if st.button("afficher le type du dataset"):
    st.write(type(data))
if st.button("les types des clonnes sélectionnés"):
    st.write(data.dtypes)
    
if st.button("La shape du dataset"):
    st.write(data.shape)
    
if st.button("affichage des statistiques descriptives"):
    st.write(data.describe().T)
    
#Représentation graphique   
st.subheader("Repésentation Graphique")
st.subheader("Heatmap et matrice de corrélation")
if st.checkbox("afficher le heatmap"):
    corr = data.corr()
    mask = np.zeros_like(corr, dtype = np.bool)
    mask[np.triu_indices_from(mask)] = True
    st.write(sns.heatmap(corr, mask = mask,  linewidths = .5 ,cmap='Greens'))
    st.pyplot()
    if st.button("afficher la matrcice de corrélation"):
        sort = corr.abs().unstack()
        sort = sort.sort_values(kind = "quicksort", ascending = False)
        st.write(sort[(sort > 0.7) & (sort < 1)])
    
        
st.subheader("Un graphique en barres afin de visualiser la taille du dataset")

if st.button("diagramme en barre"):
    f,(ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (15, 7.2))
    df_with_LIFD = data.loc[data['LIFD'] == 1]
    df_with_NLIFD = data.loc[data['LIFD'] == 0]

    sns.distplot(data['Underweight'], ax=ax1)
    sns.distplot( df_with_LIFD['Underweight'],ax = ax2 , color = 'r')
    sns.distplot( df_with_NLIFD['Underweight'],ax = ax2, color = 'g')

    df = data.loc[:,['LIFD','Underweight']]
    df['maxunder'] = df.groupby('LIFD')['Underweight'].transform('mean')
    df = df.drop('Underweight', axis=1).drop_duplicates()
    df = data.loc[:,['LIFD','Underweight']]
    df['maxunder'] = df.groupby('LIFD')['Underweight'].transform('mean')
    df = df.drop('Underweight', axis=1).drop_duplicates()

    fig = sns.barplot(data=df, x='LIFD', y='maxunder')
    fig.set(xticklabels = ['Not LIFD', 'LIFD'])
    st.write(plt.show())
    st.pyplot()

st.subheader("Choix de Digramme")

option=st.selectbox('Quelle digramme voulez vous afficher ?',('','Heatmap', 'Diagramme en bare'))

if(option=='Heatmap'):
    corr = data.corr()
    mask = np.zeros_like(corr, dtype = np.bool)
    mask[np.triu_indices_from(mask)] = True
    st.write(sns.heatmap(corr, mask = mask,  linewidths = .5 ,cmap='Greens'))
    st.pyplot()
    
elif(option==''):
    st.write(plt.show())    
else:
    f,(ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (15, 7.2))
    df_with_LIFD = data.loc[data['LIFD'] == 1]
    df_with_NLIFD = data.loc[data['LIFD'] == 0]

    sns.distplot(data['Underweight'], ax=ax1)
    sns.distplot( df_with_LIFD['Underweight'],ax = ax2 , color = 'r')
    sns.distplot( df_with_NLIFD['Underweight'],ax = ax2, color = 'g')

    df = data.loc[:,['LIFD','Underweight']]
    df['maxunder'] = df.groupby('LIFD')['Underweight'].transform('mean')
    df = df.drop('Underweight', axis=1).drop_duplicates()
    df = data.loc[:,['LIFD','Underweight']]
    df['maxunder'] = df.groupby('LIFD')['Underweight'].transform('mean')
    df = df.drop('Underweight', axis=1).drop_duplicates()

    fig = sns.barplot(data=df, x='LIFD', y='maxunder')
    fig.set(xticklabels = ['Not LIFD', 'LIFD'])
    st.write(plt.show())
    st.pyplot()

     





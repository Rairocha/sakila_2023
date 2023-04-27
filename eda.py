# Import python modules 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
    
# Immport user modules
from engine import get_engine
from functions import get_daily_rentals, get_benefits,get_movies

# sns.set_theme(style="darkgrid")

def eda():
    
    password = st.text_input("Restricted access, please enter your password: ", type="password")
    if ( password ):


        data = get_daily_rentals(get_engine(password))
        # criar o plot de linhas
        fig1, ax1 = plt.subplots(figsize=(20,10))
        # usar sns.lineplot
        #ax1.plot(x = data['data'],y=data['qtd_alugueis'],color=['red' if s == 1 else 'blue' for s in data['store_id']])
        sns.lineplot(x='data',y='qtd_alugueis',hue='store_id',data=data,ax=ax1,palette='rainbow')
        ax1.set_title("Alugueis diários para cada loja")
        st.pyplot(fig1)
        
        data = get_benefits(get_engine(password))
        # criar o plot de linhas
        fig2, ax2 = plt.subplots(figsize=(20,10))
        # usar sns.barplot
        sns.barplot(x= 'store_id',y='SUM(amount)',data=data,ax=ax2)
        ax2.set_title("Benefícios por loja")
        st.pyplot(fig2)
        
        data = get_movies(get_engine(password))
        # plotar o dataframe de filmes mais alugados por loja 
        st.dataframe(data)
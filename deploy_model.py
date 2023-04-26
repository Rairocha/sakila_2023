###############################
# This program lets you       #
# - Create a dashboard        #
# - Every dashboard page is  #
# created in a separate file  #  
###############################

# Python libraries
import streamlit as st
from PIL import Image

# User module files
from eda import eda

def main():
  
    #############  
    # Main page #
    #############   
    
    options = ['Introdução','EDA']
    choice = st.sidebar.selectbox("Menu",options, key = '1')
    
    if ( choice == 'Introdução' ):
      st.title("Análise de aluguel de filmes!")
      st.image('images/blockbuster.jpg')
      pass
    
    elif ( choice == 'EDA' ):
      eda()
      pass
      
    
main()

import pandas as pd
import scipy.stats
import streamlit as st
import time
import plotly.express as px

# Configuração da página e cabeçalho
st.set_page_config(page_title="Vehicle Data Analysis Dashboard", page_icon="🚗", layout="wide")

# Cabeçalho da aplicação
st.title("🚗 Vehicle Data Analysis Dashboard")
st.markdown("---")
st.markdown("""
**Análise Interativa de Dados de Veículos**

Esta aplicação fornece ferramentas de visualização interativa para analisar dados de vendas de veículos. 
Explore a relação entre quilometragem e preços através de histogramas e gráficos de dispersão.

**Funcionalidades:**
- Criação interativa de histogramas para dados de odômetro
- Visualização de gráfico de dispersão: odômetro vs preço
- Interface amigável com botões e caixas de seleção

*Autor: Roberto Moreno | Data: 2025-09-27*
""")
st.markdown("---")

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')
    
    fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
    st.plotly_chart(fig, use_container_width=True)
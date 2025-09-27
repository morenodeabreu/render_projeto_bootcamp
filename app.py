import pandas as pd
import streamlit as st
import plotly.express as px

# --- Configuração da página ---
st.set_page_config(page_title="Vehicle Data Analysis Dashboard",
                page_icon="🚗", layout="wide")

# --- Cabeçalho da aplicação ---
st.title("🚗 Vehicle Data Analysis Dashboard")
st.markdown("---")
st.markdown("""
**Análise Interativa de Dados de Veículos**

Esta aplicação fornece ferramentas de visualização interativa para analisar dados de vendas de veículos.
Explore a relação entre quilometragem e preços através de histogramas e gráficos de dispersão.

*Autor: Roberto Moreno | Data: 2025-09-27*
""")
st.markdown("---")

# --- Leitura do CSV com tratamento simples de erro ---
try:
    car_data = pd.read_csv('vehicles.csv')
except FileNotFoundError:
    st.error("Arquivo 'vehicles.csv' não encontrado. Coloque o arquivo na raiz do projeto.")
    st.stop()

# --- Controle 1: botão para criar histograma ---
hist_button = st.button('Criar histograma de Odometer')

if hist_button:
    st.write('Gerando histograma para a coluna `odometer`...')
    if "odometer" not in car_data.columns:
        st.warning("A coluna 'odometer' não está presente no arquivo.")
    else:
        fig_hist = px.histogram(car_data,
                                x="odometer",
                                title="Histograma de Odometer",
                                nbins=30,
                                color_discrete_sequence=['#636EFA'])
        st.plotly_chart(fig_hist, use_container_width=True)

# --- Controle 2: checkbox para criar gráfico de dispersão ---
scatter_checkbox = st.checkbox('Criar gráfico de dispersão: Odometer vs Price')

if scatter_checkbox:
    st.write('Gerando gráfico de dispersão: odometer vs price...')
    if ("odometer" not in car_data.columns) or ("price" not in car_data.columns):
        st.warning("As colunas 'odometer' e/ou 'price' não estão disponíveis no arquivo.")
    else:
        hover_cols = []
        if "year" in car_data.columns:
            hover_cols.append("year")
        if "manufacturer" in car_data.columns:
            hover_cols.append("manufacturer")

        fig_scatter = px.scatter(car_data,
                                x="odometer",
                                y="price",
                                title="Odometer vs Price",
                                hover_data=hover_cols,
                                color_discrete_sequence=['#EF553B'])
        st.plotly_chart(fig_scatter, use_container_width=True)
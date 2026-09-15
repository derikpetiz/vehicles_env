import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho da aplicação
st.header('Dashboard de Análise de Vendas de Veículos')

# Carregar os dados de veículos
car_data = pd.read_csv('vehicles.csv')

# Botão para criar o Histograma
hist_button = st.button('Criar histograma')

if hist_button:
    # Escrever mensagem explicativa
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # Criar histograma da coluna odometer
    fig = px.histogram(car_data, x="odometer")

    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção (checkbox) para o Gráfico de Dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão (Preço vs Odômetro)')

if build_scatter:
    # Escrever mensagem explicativa
    st.write('Criando gráfico de dispersão comparando Preço e Quilometragem')

    # Criar gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

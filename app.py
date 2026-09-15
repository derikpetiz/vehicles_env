import pandas as pd
import plotly.express as px
import streamlit as st

# Configuração da página (Título na aba e layout amplo)
st.set_page_config(page_title="Car Sales Dashboard", layout="wide")

# 1. Cabeçalho Principal e Descrição
st.title('🚗 Dashboard de Análise de Vendas de Veículos')
st.markdown(
    'Esta aplicação permite explorar e analisar os anúncios de vendas de carros nos EUA.')

# 2. Carregamento e Preparação dos Dados


@st.cache_data
def load_data():
    data = pd.read_csv('vehicles.csv')
    # Extrair fabricante (primeira palavra da coluna model)
    data['manufacturer'] = data['model'].apply(
        lambda x: x.split()[0] if isinstance(x, str) else 'Outros')
    return data


car_data = load_data()

# 3. Métricas Principais (Cards)
st.subheader('📊 Visão Geral do Mercado')
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Anúncios", f"{len(car_data):,}")
col2.metric("Preço Médio", f"${car_data['price'].mean():,.2f}")
col3.metric("Km Médio (Odômetro)", f"{car_data['odometer'].mean():,.0f} mi")
col4.metric("Ano Médio", f"{int(car_data['model_year'].dropna().mean())}")

st.divider()

# 4. Controles Interativos (Caixas de seleção / Checkboxes)
st.subheader('📈 Visualização de Gráficos')

show_histogram = st.checkbox('Exibir Histograma de Quilometragem', value=True)
show_scatter = st.checkbox(
    'Exibir Gráfico de Dispersão (Preço vs. Quilometragem)')
show_bar = st.checkbox('Exibir Tipos de Veículos por Fabricante')

# 5. Renderização dos Gráficos

if show_histogram:
    st.write('### Distribuição da Quilometragem dos Veículos (Odômetro)')
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribuição do Odômetro",
        labels={
            'odometer': 'Quilometragem (milhas)', 'count': 'Quantidade de Veículos'},
        color_discrete_sequence=['#1f77b4']
    )
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('### Relação entre Preço e Quilometragem')
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        title="Preço vs. Odômetro por Condição do Veículo",
        labels={'odometer': 'Quilometragem',
                'price': 'Preço (USD)', 'condition': 'Condição'},
        hover_data=['model', 'model_year']
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

if show_bar:
    st.write('### Quantidade de Veículos por Tipos e Fabricante')
    fig_bar = px.histogram(
        car_data,
        x="manufacturer",
        color="type",
        title="Tipos de Veículo por Fabricante",
        labels={'manufacturer': 'Fabricante', 'count': 'Quantidade'},
        barmode="stack"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# 6. Tabela de Dados Interativa
if st.checkbox('Mostrar Tabela de Dados Brutos'):
    st.write('### Dados dos Anúncios')
    st.dataframe(car_data.head(100))

# Dashboard de Análise de Vendas de Veículos 🚗

Esta é uma aplicação web interativa desenvolvida em Python e Streamlit para análise exploratória de dados de anúncios de vendas de carros nos Estados Unidos.

## 🚀 Funcionalidades
- **Visão Geral do Mercado (Métricas)**: Cards interativos exibindo o total de anúncios, preço médio, quilometragem média e ano médio dos veículos.
- **Histograma de Quilometragem**: Distribuição interativa do odômetro dos veículos.
- **Gráfico de Dispersão (Preço vs. Odômetro)**: Análise comparativa entre preço e quilometragem, colorida pela condição do veículo.
- **Gráfico de Barras por Fabricante**: Visualização da quantidade e tipo de veículos agrupados por fabricante.
- **Tabela de Dados Brutos**: Opção para consultar e explorar as primeiras 100 linhas do conjunto de dados.
- **Controles Interativos**: Interface dinâmica com caixas de seleção (checkboxes) para personalizar a exibição dos gráficos.

## 🛠️ Tecnologias
- Python 3
- Pandas
- Plotly Express
- Streamlit

## 📊 Análise Visual & Principais Insights

### 1. Relação entre Preço, Ano do Modelo e Condição
![Distribuição de Preço por Condição](assets/price_vs_condition.png)

* **Hipótese:** Veículos em condição "excelente" ou "como novo" apresentam menor desvalorização acumulada ao longo dos anos.
* **Conclusão:** Foi identificada uma queda acentuada no valor nos primeiros 5 anos de uso, estabilizando-se em seguida. Veículos com condição regular/boa sofrem desvalorização cerca de 15% a 20% mais rápida no mercado secundário.

### 2. Impacto da Quilometragem no Valor de Venda
![Preço vs Quilometragem](assets/price_vs_odometer.png)

* **Insight Chave:** A relação entre quilometragem e preço não é estritamente linear; há patamares de perda de valor acentuados ao ultrapassar as marcas de 50.000 e 100.000 milhas.

## 🔗 Aplicação Online
Acesse o dashboard publicado no Render: https://vehicles-env-8623.onrender.com/

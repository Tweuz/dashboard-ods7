# Nome do arquivo: app.py

# 1. Importar as bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px

# 2. Configurar a página
# Isso define o título que aparece na aba do navegador e usa o layout "wide" para ocupar a tela inteira.
st.set_page_config(page_title="Dashboard ODS 7", layout="wide")

# 3. Carregar os dados
# Esta função lê o nosso arquivo CSV. O @st.cache_data garante que os dados sejam carregados só uma vez.
@st.cache_data
def carregar_dados():
    df = pd.read_csv('acesso_eletricidade_limpo.csv')
    return df

df = carregar_dados()

# 4. Construir a interface do dashboard

# Título principal que aparece na página.
st.title("🌍 Dashboard ODS 7 - Acesso à Eletricidade")

# Barra lateral para os filtros.
st.sidebar.header("Filtros")

# Cria a lista de países para o menu de seleção, em ordem alfabética.
lista_paises = sorted(df['Pais'].unique())

# Cria o menu de seleção na barra lateral. O usuário pode escolher vários países.
paises_selecionados = st.sidebar.multiselect(
    label="Escolha os países para visualizar:",
    options=lista_paises,
    default=['Brazil', 'United States', 'China', 'Germany', 'South Africa'] # Países que já aparecem selecionados.
)

# 5. Criar as visualizações (gráfico e tabela)

# Filtra o DataFrame para conter apenas os dados dos países que o usuário escolheu.
df_filtrado = df[df['Pais'].isin(paises_selecionados)]

# Cria o gráfico de linha interativo com Plotly.
fig = px.line(
    df_filtrado,
    x='Ano',
    y='Percentual_Acesso',
    color='Pais', # Cria uma linha de cor diferente para cada país.
    title='Evolução do Acesso à Eletricidade nos Países Selecionados',
    labels={'Percentual_Acesso': '% da População com Acesso'}
)

# Mostra o gráfico na página.
st.plotly_chart(fig, use_container_width=True)

# Mostra a tabela de dados abaixo do gráfico.
st.dataframe(df_filtrado)
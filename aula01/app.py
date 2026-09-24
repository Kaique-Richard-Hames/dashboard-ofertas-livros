"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados


st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")

livros = dados.ler_livros()
qnt_livros = len(livros)
preco_medio = dados.calcular_preco_medio(livros)
qnt_cinco_estrelas = dados.contar_cinco_estrelas(livros)

col1, col2, col3 = st.columns(3)
col1.metric("Total de livros", qnt_livros)
col2.metric("Preço médio dos livros", f"£{round(preco_medio, 2)}")
col3.metric("Quantidade de livros com 5 estrelas", qnt_cinco_estrelas)

st.dataframe(livros)

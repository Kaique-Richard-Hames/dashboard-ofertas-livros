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
preco_mais_caro: float = dados.preco_item_mais_caro(livros)
titulo_mais_caro: str = dados.item_mais_caro(livros)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de livros", qnt_livros)
col2.metric("Preço médio dos livros", f"£{round(preco_medio, 2)}")
col3.metric("Quantidade de livros com 5 estrelas", qnt_cinco_estrelas)
col4.metric("Preço livro mais caro", f"£{round(preco_mais_caro, 2)}")
col4.caption(f"Título: {titulo_mais_caro}")

st.dataframe(livros)

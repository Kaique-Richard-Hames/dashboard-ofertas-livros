"""Leitura dos arquivos CSV do projeto.
"""

import csv
from pathlib import Path
from sys import exception

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except exception as error:
        print("Erro ao ler o arquivo.", error)

    return livros

def calcular_preco_medio(livros):
    total = 0
    for livro in livros:
        num_limpo: str = livro["preco"].replace("£","")
        total += float(num_limpo)
    return total / len(livros)

def contar_cinco_estrelas(livros):
    total = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if nota_limpa == "five":
            total += 1
    return total

def preco_item_mais_caro(livros):
    mais_caro: float = 0
    for livro in livros:
        str_limpa: str = livro["preco"].replace("£","")
        num_limpo: float = float(str_limpa)
        if num_limpo > mais_caro:
            mais_caro = num_limpo
    return mais_caro

def item_mais_caro(livros):
    mais_caro: float = 0
    titulo: str
    for livro in livros:
        str_limpa: str = livro["preco"].replace("£","")
        num_limpo: float = float(str_limpa)
        if num_limpo > mais_caro:
            titulo = livro["titulo"]
    return titulo

if __name__ == "__main__":
    livros = ler_livros()
    # print(f"Quantidade de livros é de: {len(livros)} livros.")
    # print(f"Preço médio dos livros: {round(calcular_preco_medio(livros), 2)} libras.")
    # print(f"Quantidade de livros com 5 estrelas: {contar_cinco_estrelas(livros)}")

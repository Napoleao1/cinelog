import os
import json
from datetime import date

ARQUIVO_DADOS = "meus_filmes.json"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def obter_ano_valido():
    while True:
        try:
            ano = int(input("Ano de lancamento: "))

            if ano < 1888 or ano > date.today().year:
                print("Por favor, digite um ano realista")
                continue

            return ano

        except ValueError:
            print("Erro: digite apenas numeros inteiros para o ano")


def obter_nota_valida():
    while True:
        try:
            nota = float(input("Nota (0.0 a 5.0): "))
            if nota < 0.0 or nota > 5.0:
                print("A nota deve estar entre 0 e 5.")
                continue

            return nota
        except ValueError:
            print("Digite um valor numerico (use ponto para decimais)")


def adicionar_filme(catalogo):
    limpar_tela()
    titulo = input("Titulo: ").strip()

    for filme in catalogo:
        if filme["titulo"].lower() == titulo.lower():
            print(f"\nAtencao: O filme '{filme['titulo']}' ja esta cadastrado no catalogo")
            return

    genero = input("Genero: ").strip()
    ano = obter_ano_valido()
    nota = obter_nota_valida()
    critica = input("Breve critica: ").strip()

    filme = {
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "nota": nota,
        "critica": critica,
    }

    catalogo.append(filme)
    salvar_dados(catalogo)
    print(f"{titulo} adicionado com sucesso ao seu catalogo")


def listar_filmes(catalogo):
    limpar_tela()
    print("=" * 40)
    print("           MINHA COLECAO")
    print("=" * 40)

    if not catalogo:
        print("Nao possui filmes cadastrados no catalogo")
        print("=" * 40)
        return

    for filme in catalogo:
        estrelas = "*" * int(filme["nota"])
        genero = filme.get("genero", "Desconhecido")
        titulo = filme["titulo"].upper()
        ano = filme["ano"]
        nota = filme["nota"]

        print(f"[{ano}] {titulo} ({genero}) | Nota: {nota:.1f} {estrelas}")
        print("=" * 40)


def pesquisar_por_titulo(catalogo):
    limpar_tela()
    termo = input("Digite parte do titulo para pesquisar: ").strip().lower()

    resultados = []
    for filme in catalogo:
        if termo in filme["titulo"].lower():
            resultados.append(filme)

    _exibir_resultados_pesquisa(resultados)


def pesquisar_por_ano(catalogo):
    limpar_tela()
    try:
        ano_pesquisa = int(input("Digite o ano de lancamento exato para pesquisar: "))
    except ValueError:
        print("Erro: Digite um numero valido (numero inteiro)")
        return

    resultados = []
    for filme in catalogo:
        if filme["ano"] == ano_pesquisa:
            resultados.append(filme)

    _exibir_resultados_pesquisa(resultados)


def pesquisar_por_genero(catalogo):
    limpar_tela()
    termo = input("Digite o genero para pesquisar (ex: acao): ").strip().lower()

    resultados = []
    for filme in catalogo:
        if termo in filme.get("genero", "").lower():
            resultados.append(filme)

    _exibir_resultados_pesquisa(resultados)


def _exibir_resultados_pesquisa(resultados):
    if resultados:
        print(f"\nEncontrados {len(resultados)} resultado(s):")
        for filme in resultados:
            genero = filme.get("genero", "Desconhecido")
            print(f"> {filme['titulo']} ({filme['ano']}) - {genero} - Nota: {filme['nota']}")
    else:
        print("\nNenhum filme encontrado com esses criterios.")

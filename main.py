import catalogo


def mostrar_menu():
    catalogo.limpar_tela()
    print("\n" + "=" * 40)
    print("              CINELOG")
    print("=" * 40)
    print("1. Adicionar filme/serie")
    print("2. Listar filmes")
    print("3. Pesquisar por titulo")
    print("4. Pesquisar por genero")
    print("5. Pesquisar por ano")
    print("6. Sair")
    print("=" * 40)


def iniciar_app():
    meus_filmes = catalogo.carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ")

        match opcao:
            case "1":
                catalogo.adicionar_filme(meus_filmes)
                input("\nPressione Enter para voltar ao menu...")

            case "2":
                catalogo.listar_filmes(meus_filmes)
                input("\nPressione Enter para voltar ao menu...")

            case "3":
                catalogo.pesquisar_por_titulo(meus_filmes)
                input("\nPressione Enter para voltar ao menu...")

            case "4":
                catalogo.pesquisar_por_genero(meus_filmes)
                input("\nPressione Enter para voltar ao menu...")

            case "5":
                catalogo.pesquisar_por_ano(meus_filmes)
                input("\nPressione Enter para voltar ao menu...")

            case "6":
                catalogo.limpar_tela()
                catalogo.salvar_dados(meus_filmes)
                print("Ate logo!")
                break

            case _:
                print("Opcao invalida")
                input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    iniciar_app()

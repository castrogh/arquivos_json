from funcoes import *

usuarios = {}
opcao = menu()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
        opcao = menu()
    
    if opcao == "P":
        pesquisar(usuarios, input("Digite o login que deseja pesquisar: "))
        print(pesquisar(usuarios))
        opcao = menu()


    if opcao == "E":
        excluir(usuarios, input("Digite o login que deseja excluir: "))
        opcao = menu()

    if opcao == "L":
        listar(usuarios)
        opcao = menu()
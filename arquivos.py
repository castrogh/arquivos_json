with open("logs.txt", "w") as arquivo:
    arquivo.write("#### REGISTROS DE LOGS #####")

resposta = "S"
while resposta == "S":
    with open("logs.txt", "a") as arquivo:
        arquivo.write(input("\nDigite o registro desejado: "))
    resposta = input("\nDeseja adicionar mais logs? S/N ").upper()
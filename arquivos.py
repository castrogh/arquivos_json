with open("logs.txt", "w") as arquivo:
    arquivo.write("#### REGISTROS DE LOGS #####\n")

resposta = "S"
while resposta == "S":
    with open("logs.txt", "a") as arquivo: #com o parâmetro a (append) é possível adicionar novas informações ao arquivo, sem que perder o que já estava nele
        arquivo.write(input("\nDigite o registro desejado: ") + "\n")
    resposta = input("\nDeseja adicionar mais logs? S/N ").upper()

with open("logs.txt", "r") as arquivo:
    conteudo = arquivo.read() #o método read lê o arquivo como um todo, ou seja, apresenta todo conteúdo do ao arquivo ao ser printado na tela
    print(conteudo)
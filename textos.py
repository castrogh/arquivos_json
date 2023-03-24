txt = "Baby baby do baby do biruleibe leibe"
print (txt[0:4])

print (txt[21:])#ao não indicar uma posição final, deixando apenas o :, o Python vai ler todas as demais posições, até a última, à partir da posição informada

print (txt[21:30])

print (txt[::-1])#exibe o texto ao contrário

print (txt[0:4:2])
#posição inicial (0) : qtde de caracteres a ser lida (4) : passo (2), que define de qtas em qtas posições o Python vai ler a string

#strings também podem ser tratadas como listas, a manipulação é feita através do [] e indicando a posição do caractere que deseja
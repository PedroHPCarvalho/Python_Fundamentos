arquivo = open("C:/Users/pedro/Documents/Python Scripts/Python_Fundamentos/FILE_MANIPULATION/FILES/fileTest1.txt")

# read - faz a leitura totelmente, armazenando todo o arquivo na memória
# print(arquivo.read())

# readline - faz a leitura do arquivo uma linha de cada vez
# print(arquivo.readline())

# readlines - faz a leitura do arquivo inteiro e armazena em uma lista
# print(arquivo.readlines())

# itera sobre a lista vindo do readlines, printando uma de cada vez
# for linha in arquivo.readlines():
#   print(linha)

#dica - um script rapido para ler arquivos
while len(linha := arquivo.readline()):
  print(linha)

arquivo.close()
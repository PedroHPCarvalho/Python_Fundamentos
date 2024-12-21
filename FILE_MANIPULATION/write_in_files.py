file = open("C:/Users/pedro/Documents/Python Scripts/Python_Fundamentos/FILE_MANIPULATION/FILES/fileTest2.txt" , "w")
#escreve no arquivo
file.write("Hello World")

obj_interavel = ["\nBOM DIA AMIGOS\n","DEUS e FIEL\n","MENSAGEM ALEATORIA\n"]

#escreve no arquivo a partir de um objeto iteravel
file.writelines(obj_interavel)
file.close()
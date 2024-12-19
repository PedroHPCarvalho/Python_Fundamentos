#Nesse exemplo, vamos relembrar sobre o uso de funcoes como argumentos

def dar_bomdia (nome):
  return f"Bom dia {nome}"

def mensagem_pos_bomdia(texto):
  return f"{texto}".upper()

def exibir_mensagem(funcao1,funcao2):
  print(f"{(funcao1)}, {(funcao2)}")

exibir_mensagem(dar_bomdia("Pedro"),mensagem_pos_bomdia("Vamos começar o dia estudando"))
#Bom dia Pedro, VAMOS COMEÇAR O DIA ESTUDANDO

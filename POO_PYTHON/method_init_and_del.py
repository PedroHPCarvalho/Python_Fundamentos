class Cachorro:
  def __init__(self,nome,cor,acordado=True):
    print("Iniciando a Classe...")
    self.nome = nome
    self.cor = cor
    self.acordado = acordado

  def __del__ (self):
    print("Destruindo Instancia da Classe...")

  def latir(self):
    print("auau")


cachoro = Cachorro("doki","branco")
cachoro.latir()
del cachoro
print("Código sendo executado...")
print("Código sendo executado...")
print("Código sendo executado...")
print("Código sendo executado...")
print("Código sendo executado...")

print()

cachoro = Cachorro("doki","branco")
cachoro.latir()
print("Código sendo executado...")
print("Código sendo executado...")
print("Código sendo executado...")
print("Código sendo executado...")
print("Código sendo executado...")
del cachoro

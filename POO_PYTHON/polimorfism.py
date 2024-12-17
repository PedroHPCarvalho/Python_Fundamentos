class Voador:
  def voar(self):
    print ("Voar")

class Passaro(Voador):
  def voar(self):
    print("Passaros Voam")

class Pardal(Passaro):
  def voar(self):
    return super().voar()
  
class Avestruz(Passaro):
  def voar(self):
    print("Avestruz não voam")

voador = Voador()
voador.voar()
print()
passaro = Passaro()
passaro.voar()
print()
avestruz = Avestruz()
avestruz.voar()
print()
pardal = Pardal()
pardal.voar()
def meu_gerador(numeros: list[int]):
  for numero in numeros:
    yield numero * 3


for i in meu_gerador(numeros=[1,2,3,5,10,23]):
  print(i)
#union - faz a uniao de 2 conjuntos
conjunto_A = {1,2,3}
conjunto_B = {3,4,1}

conjunto_uniao = conjunto_A.union(conjunto_B)
print(conjunto_uniao)
print()

#intersection - pega os valores em comum dos dois conjuntos
conjunto_interseccao=conjunto_A.intersection(conjunto_B)
print(conjunto_interseccao)
print()

#difference - mostra a os valores diferentes entre os conjuntos
conjunto_diferenca=conjunto_A.difference(conjunto_B)
print(conjunto_diferenca)
print()

#symetric_difference - mostra a os valores diferentes entre os conjuntos
conjunto_simetrica_diferenca=conjunto_A.symmetric_difference(conjunto_B)
print(conjunto_simetrica_diferenca)
print()

#issubset - verifica se um conjunto é subconjunto de outro
conjunto_subconjunto= conjunto_A.issubset(conjunto_B)
print(conjunto_subconjunto)
print()

#issuperset
conjunto_issuper = conjunto_A.issuperset(conjunto_B)
print(conjunto_issuper)
print()

#isdsjoint
conjunto_isdisjoint=conjunto_A.isdisjoint(conjunto_B)
print()

#add item no set
conjunto_add = {1,3}
print(conjunto_add)
conjunto_add.add(7)
print(conjunto_add)
print()

#clear - limpa o conjunto
conjunto_clear = {1,3}
print(conjunto_clear)
conjunto_clear.clear()
print(conjunto_clear)
print()

#discard e remove - discarta um elemento informado
conjunto_discard = {1,3}
print(conjunto_discard)
conjunto_discard.discard(1)
print(conjunto_discard)
print()

#pop - apaga p ultimo elemento se n for informado o indice
conjunto_pop = {1,3}
print(conjunto_pop)
conjunto_pop.pop()
print(conjunto_pop)
print()

#in - verifica se um item esta dentro do conjunto
conjunto_in = {1,3}
print(conjunto_in)
print(1 in conjunto_in)
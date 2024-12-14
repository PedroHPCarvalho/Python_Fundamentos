#alguns metodos da classe list

#append - adiciona novos elementos na lista 
lista_append = []

lista_append.append(1)
lista_append.append("Bom dia")
lista_append.append([10,23,42])

print(lista_append)

print()
#clear- limpa uma lista, retirando todos seus elementos

lista_clear = [12,312,341,342]
print(lista_clear)
lista_clear.clear()
print(lista_clear)

print()

#copy - faz uma copia da lista
lista_copy = ["Python",123,34214]
lista_copy.copy()
print(lista_copy)
print()

#count - conta quantas vezes um elemento se repete
lista_count=["vermelho","verde","azul","verde","azul"]
print(lista_count.count("vermelho"))
print(lista_count.count("verde"))
print()

#extends - extende uma lista, adicionando os termos ao final dela
lista_extend=[12,343,213]
print(lista_extend)
lista_extend.extend(["Bom dia"])
print()

#index - saber o index de um determinado elemento
lista_index=[123,3124,4123,1]
print(lista_index.index(1))
print()

#pop - retira elementos da lista, se nao for expecificado qual tirar ele retira o ultimo termo
lista_pop = ["a","b","c","d"]
print(lista_pop)
lista_pop.pop(0)
print(lista_pop)
lista_pop.pop()
print(lista_pop)
lista_pop.pop()
print(lista_pop)

print()

#remove - retira elemento da lista, precisa ser especificado
lista_remove = ["a","b","c","d"]
print(lista_remove)
lista_remove.remove("a")
print(lista_remove)
print()

#reverse - mostra a lista de traz pra frente, do ultimo indice ate o 0
lista_reverse = ["a","b","c","d"]
print(lista_reverse)
lista_reverse.reverse()
print(lista_reverse)

print()

#sort e sorted ordena a lista de acordo com os parametros
lista_sort = ["a","b","c","d"]
lista_sort.sort()
print(lista_sort)

lista_sort = ["a","b","c","d"]
lista_sort.sort(reverse=True)
print(lista_sort)

lista_sort = ["aa","b","ccc","dddd"]
lista_sort.sort(key=lambda x:len(x))
print(lista_sort)

lista_sort = ["aa","b","ccc","dddd"]
lista_sort.sort(key=lambda x:len(x),reverse=True)
print(lista_sort)

print()
#len saber o tamanho de uma lista
lista_len = [1,2,23,4,5,6,6,87,5]
print(lista_len.__len__())
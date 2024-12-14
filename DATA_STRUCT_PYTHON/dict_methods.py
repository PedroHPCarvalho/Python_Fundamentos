#clear - limpa o dicionario
dict_clear = {"nome":"Pedro","carro":"livinia"}
print(dict_clear)
dict_clear.clear()
print(dict_clear)
print()

#copy - cria uma copia do dicionario
dict_copy = {"nome":"Pedro","carro":"livinia"}
print(dict_copy)
copia = dict_copy.copy()
copia["nome"]="Ana"
print(copia)
print()

#fromkeys - O método fromkeys() em Python é uma forma rápida de criar um novo dicionário a partir de uma lista de chaves e um valor inicial. 
#Cada chave da lista é mapeada para o mesmo valor inicial no novo dicionário.
dict_fromkeys = {"nome":"Pedro","carro":"livinia"}
print(dict_fromkeys.fromkeys(["nome","carro"]))
print()

#get - pega items
dict_get = {"Pedro" : {"idade": 21, "namorada": "Ana"}}
print(dict_get.get("Pedro"))
print()

#items - mostra os items de um dicionario
dict_items = {"Pedro" : {"idade": 21, "namorada": "Ana"}}
print(dict_items.items())
print()

#keys - ver suas chaves
dict_keys = {"Pedro" : {"idade": 21, "namorada": "Ana"}}
print(dict_keys.keys())
print()

#pop - deleta items e a chave
dict_pop = {"nome":"Pedro","carro":"livinia"}
dict_pop.pop("nome")
print(dict_pop)
print()

#popitem
dict_popitems = {"nome":"Pedro","carro":"livinia"}
dict_popitems.popitem()
print(dict_popitems)
print()

#setdefault - seta um padrão
dict_setdefault = {"nome":"Pedro","carro":"livinia"}
dict_setdefault.setdefault("nome", "anonimo")
print()

#update - atualiza os valores 
dict_update = {"nome":"Pedro","carro":"livinia"}
dict_update.update({"nome": "Carvalho"})
print(dict_update)
print()

#values - lista os valores
dict_values = {"nome":"Pedro","carro":"livinia"}
print(dict_values.values())
print()

#in
dict_in = {"Pedro" : {"idade": 21, "namorada": "Ana"}}
print("Pedro" in dict_in)
print()

#del
dict_del = {"Pedro" : {"idade": 21, "namorada": "Ana"}}
print(dict_del)
del dict_del["Pedro"]["idade"]
print(dict_del)
print()
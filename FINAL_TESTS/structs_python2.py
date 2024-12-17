# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:
def elementos_comuns(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    return list(set1.intersection(set2))
    
# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# print(f"{lista1}\n{lista2}")

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1,lista2)
    comuns_int = list(map(int,comuns))
    comuns_int.sort()
    print(f"Elementos comuns às duas listas: {comuns_int}")
else:
    print("Entrada inválida.")
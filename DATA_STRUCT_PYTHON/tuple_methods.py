# count - conta quantas vezes um elemento se repete
tuple_count = (1,2,3,4,5,5,5,3,1,2,3,4,3,)
print(tuple_count.count(1))
print(tuple_count.count(2))
print(tuple_count.count(3))
print(tuple_count.count(4))
print(tuple_count.count(5))

print()

#index - verifica o index de um elemento na tupla
tuple_index = (1,2,3,4,5,5,5,3,1,2,3,4,3,)
print(tuple_index.index(4))

print()

#len - mostra a quantidade de elemntos de uma tupla
tuple_len = (1,2,3,4,5,5,5,3,1,2,3,4,3,)
print(tuple_len.__len__())
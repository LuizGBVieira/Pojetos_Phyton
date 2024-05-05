lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

lista_soma = [a + z for a , z in zip(lista_a , lista_b)]
print(lista_soma)

print('Segunda Solução')
print() 

lista_soma1 = []
for i in range(len(lista_b)):
    lista_soma1.append(lista_a[i] + lista_b[i])
print(lista_soma1)

print()
print('Terceira Resolução') 

lista_soma2 = []
for i, _ in enumerate(lista_b):
    lista_soma2.append(lista_a[i] + lista_b[i])
print(lista_soma1)
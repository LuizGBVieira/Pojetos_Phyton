# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.
def zipper(nome_cidade , nome_estado):
    intervalo = min(len(nome_cidade), len(nome_estado))
    return [(nome_cidade[i], nome_estado[i]) for i in range(intervalo)  
            ]


nome_cidade=['Salvador', 'Ubatuba', 'Belo Horizonte']
nome_estado=['BA', 'SP', 'MG', 'RJ']
print(nome_cidade, nome_estado)
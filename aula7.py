nome = 'Jorge henrique'
nome_novo = ''
indice = 0 
while indice < len(nome):
    letra = nome[indice]
    nome_novo += f'*{letra}'
    indice += 1
    
print(nome_novo)
import copy
from dados import produtos
#produtos = [
   # {'nome': 'Produto 5', 'preco': 10.00},
 #   {'nome': 'Produto 1', 'preco': 22.32},
 #   {'nome': 'Produto 3', 'preco': 10.11},
  #  {'nome': 'Produto 2', 'preco': 105.87},
   # {'nome': 'Produto 4', 'preco': 69.90},]

novos_produtos = [
   {**p, 'preco': round(p['preco'] * 1.1, 2) }
   for p in copy.deepcopy(produtos)
]




print(*produtos, sep= '\n')
print('COM 10% A MAIS')
print()
print(*novos_produtos, sep='\n')




print('POR ORDEM DESCRESCENTE')
print()

produtos_ordenados_por_nome = sorted(
   copy.deepcopy(produtos),    
   key=lambda p: p['nome'],             
   reverse=True
) 
print(*produtos_ordenados_por_nome, sep='\n')





print('PRECO EM ORDEM CRESCENTE')
print()

produtos_ordenados_por_preco = sorted(
   copy.deepcopy(produtos),    
   key=lambda p: p['preco'],             
) 
print(*produtos_ordenados_por_preco, sep='\n')



    
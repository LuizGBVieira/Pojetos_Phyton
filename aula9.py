import os

lista = []
while True:
    print('Selecione uma opcao:')
    opcao = input('[i]nserir , [a]pagar, [l]istar.')  
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        os.system('cls')
        indice_lista = input('Selecione um valor para apagar:')

        try:
            indice = int(indice_lista)
            del lista[indice]
        except ValueError:
            print('Digite um numero inteiro!')
        except IndexError:
            print('Indice não encontrado na lista.')    
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Não a nada para listar.')
        
        for i, valor in enumerate(lista):
            print(i, valor) 
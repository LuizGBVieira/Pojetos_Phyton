entrada = input('Digite seu primeiro nome: ')
nome_quantidade =len(entrada)
if nome_quantidade >= 1:
    if nome_quantidade <= 4:
        print('Seu nome é curto!')
    elif nome_quantidade >= 5 and nome_quantidade <=6:
        print('Seu nome é normal!')
    elif nome_quantidade >= 7:
        print('Seu nome é muito grande!')
else:
    print('Digite alguma letra.')
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
nome_invertido = (nome[::-1])
nome_quantidade = (len(nome[::]))
primeira_letra = (nome[0])
ultima_letra = (nome[-1])


if nome and idade:
    print(f'seu nome é: {nome}')
    print(f'seu nome invertido é: {nome_invertido}')
    
    if ' ' in nome:   
        print('seu nome tem espaços.')
    else:
        print('Seu nome não contém espaços!')
    
    print(f'seu nome tem {nome_quantidade} letras.')
    print(f'a primeira letra do seu nome é: {primeira_letra}')
    print(f'a ultima letra do seu nome é: {ultima_letra} ')
else:
    print('Desculpe, mas você deixou campos em branco!')
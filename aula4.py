numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero) 
    par_impar = numero_int % 2 == 0
    par_impar_text = 'impar'

    if par_impar:
        par_impar_text = 'par'
        
    print(f'O numero {numero_int} é {par_impar_text}!')
else:
    print('Digite um numero inteiro.')

def numeros(numero):
    par_impar = numero % 2 == 0
    if par_impar:
        return f'O numero {numero} é par!'
    else:
        return f'O numero {numero} é ímpar!'

print(numeros(10))
print(numeros(5))
print(numeros(20))
print(numeros(100))
print(numeros(1))

    



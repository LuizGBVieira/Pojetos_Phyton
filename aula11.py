

def numeros_mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicação = numeros_mult(2, 2, 2, 2)
print(multiplicação)
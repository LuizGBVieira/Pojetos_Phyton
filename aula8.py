tentativa = input('Digite uma letra:')
palavra_secreta = 'cachorro'
letras_acertadas = ''

while True:
    if len(tentativa) > 1:
        print('Digite apenas uma letra')
        continue
    if tentativa in palavra_secreta:
        letras_acertadas =+ tentativa
        print(letras_acertadas)
    
    
    



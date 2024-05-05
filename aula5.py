hora = input('Que horas são? ')
try:
    hora_int = int(hora)
    if 0 <= hora_int <= 11:
        print('Bom dia!')
    elif 12 <= hora_int <= 17:
        print('Boa tarde!')
    elif 18 <= hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não conheço esse horario.')
except:
    print('Digite algum horario.')    
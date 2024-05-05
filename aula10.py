cpf = '74682489070'
cpf_fatiado = cpf[:9]
cpf_contador = 10

resultado_1 = 0
for digito in cpf_fatiado:
    resultado_1 += int(digito) * cpf_contador
    cpf_contador -= 1
mult_resultado = (resultado_1 * 10) % 11
mult_resultado = mult_resultado if mult_resultado <= 9 else 0
print(mult_resultado)





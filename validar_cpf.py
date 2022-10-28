import re

def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub('\D', '', cpf)

    novo_cpf = cpf[:-2]

    multiplicadores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    soma_1 = 0
    for index, valor in enumerate(novo_cpf, 1):
        valor = int(valor)
        resultado = valor * multiplicadores[index]
        soma_1 += resultado

    formula = 11 - (soma_1 % 11)
    digito_1 = 0 if formula > 9 else formula
    novo_cpf += str(digito_1)

    soma_2 = 0
    for index, valor in enumerate(novo_cpf):
        valor = int(valor)
        resultado = valor * multiplicadores[index]
        soma_2 += resultado
    
    formula = 11 - (soma_2 % 11)
    digito_2 = 0 if formula > 9 else formula
    novo_cpf += str(digito_2)

    sequencia = cpf[0] * len(cpf)
    if novo_cpf == cpf and novo_cpf != sequencia:
        return 'CPF válido!'
    else:
        return 'CPF inválido'
    
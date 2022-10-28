from random import randint


def gera_cpf():
    numeros_sorteado = randint(100000000, 999999999)
    cpf = str(numeros_sorteado)
    multiplicadores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    soma_1 = 0
    for index, valor in enumerate(cpf, 1):
        valor = int(valor)
        resultado = valor * multiplicadores[index]
        soma_1 += resultado

    formula = 11 - (soma_1 % 11)
    digito_1 = 0 if formula > 9 else formula
    cpf += str(digito_1)

    soma_2 = 0
    for index, valor in enumerate(cpf):
        valor = int(valor)
        resultado = valor * multiplicadores[index]
        soma_2 += resultado
    
    formula = 11 - (soma_2 % 11)
    digito_2 = 0 if formula > 9 else formula
    cpf += str(digito_2)
    
    return cpf

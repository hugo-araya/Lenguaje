cont = 1
positivo = 0
negativo = 0
neutro = 0
while cont <= 6:
    numero = int(input('Numero: '))
    if numero > 0:
        positivo = positivo + 1
    else:
        if numero < 0:
            negativo = negativo + 1
        else:
            neutro = neutro + 1
    cont = cont + 1
print('Positivos: ', positivo)
print('Negativos: ', negativo)
print('Neutros: ', neutro)


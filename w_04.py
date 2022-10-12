cont = 1
while cont <= 10:
    numero = int(input('Numero: '))
    if numero > 0:
        print('Es positivo')
    else:
        if numero < 0:
            print('Es negativo')
        else:
            print('Es neutro')
    cont = cont + 1

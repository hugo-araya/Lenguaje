valor = int(input('Valor: '))
marca = input('Marca: ')
if valor >= 300000:
    pagar = valor * 0.9
else:
    pagar = valor
if marca == 'YNOS':
    pagar = pagar * 0.05
pagar = pagar * 1.19
print('A pagar: ', pagar)

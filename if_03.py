cap_inv = int(input('Capital a invertir: '))
p_interes = float(input('Interes: '))
if cap_inv * p_interes > 7000:
    saldo = cap_inv + cap_inv * p_interes
else:
    saldo = cap_inv
print('Saldo final: ', saldo)


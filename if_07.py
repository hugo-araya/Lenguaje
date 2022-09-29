compra = int(input('Compra: '))
if compra > 1000:
    descuento = compra * 0.2
else:
    descuento = 0
tot_pagar = compra - descuento
print('A pagar: ', tot_pagar)

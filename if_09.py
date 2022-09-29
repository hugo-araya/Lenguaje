#Escribir un algoritmo que escriba el nombre de un articulo, 
#clave, precio original y su precio con descuento. 
#El descuento lo hace en base a la clave, 
#si la clave es 01 el descuento es del 10% y 
#si la clave es 02 el descuento es del 20% (solo existen dos claves).

nombre = input('Articulo: ')
clave = input('Clave: ')
precio = int(input('Precio: '))
if clave == '01':
    descuento = precio * 0.1
else:
    descuento = precio * 0.2
precio_desc = precio - descuento
print('Articulo: ', nombre)
print('Codigo: ', clave)
print('Precio: ', precio)
print('Oferta: ', precio_desc)


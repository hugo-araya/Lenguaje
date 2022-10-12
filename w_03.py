suma = 0
cont = 1
n = int(input('Cuantas notas son: '))
while cont <= n:
    nota = float(input('Nota : '))
    suma = suma + nota
    cont = cont + 1
promedio = suma/n
print('Promedio: ', promedio)
suma = 0
cont = 1
minima = 10
maxima = 0
n = int(input('Cuantas notas son: '))
while cont <= n:
    nota = float(input('Nota : '))
    suma = suma + nota
    if nota < minima:
        minima = nota
    if nota > maxima:
        maxima = nota
    cont = cont + 1
promedio = suma/n
print('Promedio: ', promedio)
print('Minima es: ', minima)
print('Maxima es: ', maxima)
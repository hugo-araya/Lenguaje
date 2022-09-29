nota1 = float(input('Nota 1: '))
por1 = float(input('Porcentaje nota 1: '))
nota2 = float(input('Nota 2: '))
por2 = float(input('Porcentaje nota 2: '))
nota3 = float(input('Nota 3: '))
por3 = float(input('Porcentaje nota 3: '))

por4 = float(input('Porcentaje nota 4: '))
acumulado = nota1*por1 + nota2*por2 + nota3*por3
falta = 4 - acumulado
nota = falta / por4

print('Necesita la nota: ',nota)



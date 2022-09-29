nota1 = float(input('Nota 1: '))
por1 = float(input('Porcentaje nota 1: '))
nota2 = float(input('Nota 2: '))
por2 = float(input('Porcentaje nota 2: '))
nota3 = float(input('Nota 3: '))
por3 = float(input('Porcentaje nota 3: '))
promedio = nota1*por1 + nota2*por2 + nota3*por3
mensaje = 'Alumno Reprobado'
if promedio >= 4.0:
    mensaje = 'Alumno Aprobado'
print('Estado: ',mensaje, 'con nota: ', promedio)


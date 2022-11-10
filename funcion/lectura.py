ar = open('archivo.txt')
sal = open('salida.txt', 'w')
linea = ar.readline()
while linea != '':
    linea = linea.rstrip('\n')
    sal.write(linea.upper()+'\n')
    linea = ar.readline()
ar.close()
sal.close()

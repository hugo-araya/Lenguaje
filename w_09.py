hora = 0
while hora < 24:
    minuto = 0
    while minuto < 60:
        segundo = 0
        while segundo < 60:
            print(hora,':',minuto,':', segundo)
            segundo = segundo + 1
        minuto = minuto + 1
    hora = hora + 1
print('Se acabo el dia')

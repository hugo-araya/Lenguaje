# Lo primero es generar la secuencia objetivo
# que debe contener 5 letras escogidas entre
# las letras a,b,c,d,e,f,g,h,i,j
# esto se debe realiar en una funcion y considerar 
# la utilizacion de la biblioteca random.

import random

def genera_objetivo():
    lista = ['a','b','c','d','e','f','g','h','i','j']
    i = 0
    objetivo = ''
    while i < 5:
        numero = random.randint(0,9)
        objetivo = objetivo + lista[numero]
        i = i + 1
    return objetivo

secreto = genera_objetivo()
print(secreto)

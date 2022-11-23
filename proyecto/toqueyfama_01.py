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

#print(secreto)
# A continuacion se debe crear una funcion
# que lea desde el teclado lo ingresado por
# el jugador. Debe devolver un string

def lee_usuario():
    combi = input('Combinacion: ')
    lista = combi.split(' ')
    combi = "".join(lista)
    return combi

# Otra version mas artesanal de la lectura

def lee_usuario_1():
    combi = input('Combinacion: ')
    salida = ''
    lista = combi.split(' ') 
    i = 0
    while i < len(lista):
        salida = salida + lista[i]
        i = i + 1
    return salida

combinacion = lee_usuario()
print(combinacion)

combinacion = lee_usuario_1()
print(combinacion)


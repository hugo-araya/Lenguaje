import turtle

def circulo(lado):
    i = 0
    while i < 360:
        flecha.forward(lado)
        flecha.right(1)
        i = i + 1

def triangulo(lado):
    i = 0
    while i < 3:
        flecha.forward(lado)
        flecha.right(120)
        i = i + 1

def hexagono(lado):
    i = 0
    while i < 6:
        flecha.forward(lado)
        flecha.right(60)
        i = i + 1

def cuadrado(lado):
    i = 0
    while i < 4:
        flecha.forward(lado)
        flecha.right(90)
        i = i + 1


ventana = turtle.Screen() 
flecha = turtle.Turtle() 

"""
j = 0
lado = 100
giro = 0
while j < 8:
    cuadrado(lado)
    giro = giro + 45
    flecha.right(giro)
    j = j + 1
"""
#triangulo(100)
circulo(1)
ventana.mainloop()
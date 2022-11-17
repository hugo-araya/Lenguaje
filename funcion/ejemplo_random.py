import random
#Genera objetivo con letras repetidas
objetivo=''
i = 0
while i < 5:
    objetivo = objetivo+random.choice("abcdefghijk")
    i = i + 1
print("Con repetidos",objetivo)

#Genera objetivo con letras NO repetidas
objetivo=''
i = 0
while i < 5:
    letra = random.choice("abcdefghijk")
    if letra not in objetivo:
        objetivo = objetivo + letra
        i = i + 1
print("Sin repetidos",objetivo)

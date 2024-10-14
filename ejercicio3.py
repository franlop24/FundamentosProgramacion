'''
Ejercicio 3:
    Programa que calcula la hipotenusa de un triangulo
    rectángulo a partir de sus catetos
Entradas:
    cateto1: int
    cateto2: int
Salidas:
    hipotenusa
Análisis:
    Se resuelve con el teorema de pitágoras
'''
import math
cateto1 = input("Escribe el cateto 1: ")
cateto1 = int(cateto1)
cateto2 = int(input('Escribe el cateto 2: '))
hipotenusa = cateto1 * cateto1 + cateto2 * cateto2
hipotenusa = hipotenusa ** (1/2)
hipotenusa = math.sqrt(hipotenusa)
print('La hipotenusa es: ', hipotenusa)
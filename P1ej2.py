#Prac1 ej2
import random
import numpy as N


filas=int(input("Dime numero de filas: "))
columnas=int(input("Dime numero de columnas: "))

a=N.random.rand(filas,columnas)
print(a)

print("\nEl mínimo es: ",a.min(axis=None))
print("\nEl máximo es: ",a.max(axis=None))


#falta producto escalar 2 vectores

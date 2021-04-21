#Pract1 ej3
import numpy as N

filas,columnas=3,3
matriz=N.empty((filas,columnas))
    

for i in range(filas):
    for j in range (columnas):
        matriz[i][j]=float(input("Introduce el dato: "))

print(matriz)

print("\nLos maximos por filas:")
print(matriz.max(axis=1))
print("\nLos maximos por columnas:")
print(matriz.max(axis=0))

print("\nDeterminante:")
print(N.linalg.det(matriz))

print("\nRango:")
print (N.linalg.matrix_rank(matriz));

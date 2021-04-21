#Pract1 ej4
import numpy as N
from scipy import stats as st

filas,columnas=3,3
matriz=N.empty((filas,columnas))
    
media=0
for i in range(filas):
    for j in range (columnas):
        matriz[i][j]=int(input("Introduce el dato: "))
        media=media+matriz[i][j]

print(matriz)

print("\nModa:")
print(st.mode(matriz));
print("\nMedia:")
print(media/(filas*columnas))



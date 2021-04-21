# -*- coding: utf-8 -*-
"""
Numpy examples
"""
import numpy as N
from scipy import stats as st

####################
# NumPy Array
####################

a = N.array([[1,2,3],[4,5,6]],float)
print(a);



#CHECKING THE TYPE
print (type(a));

#NUMERIC ‘TYPE’ OF ELEMENTS
print (a.dtype, a.dtype.type);

#BYTES PER ELEMENT
print(a.itemsize);

# ARRAY SHAPE
# shape returns a tuple
# listing the length of the
# array along each dimension.
print (a.shape);

#ARRAY SIZE
print (a.size);

#NUMBER OF DIMENSIONS
print (a.ndim);

#ARRAY COPY
b = a.copy();
print(b);

#CONVERSION TO LIST
c=a.tolist();
print(c);

#############################
#Setting Array Elements
#############################

#ARRAY INDEXING
print(a[0,0]);

#FILL
print(a.fill(0));

# BEWARE OF TYPE COERSION
a = N.array([[1,2,3],[4,5,6]]);
a[0] = 10.6;
print (a);

#############################
#Array Slicing
#############################
a = N.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]]);
print(a);
print(a[0,3:5]);
print( a[4:,4:]);
print(a[:,2])
print(a[2::2,::2]);

#############################
#Fancy Indexing
#############################

a = N.arange(0,80,10);
print(a);
y = a[[1, 2, -3]];
print(y);
mask = N.array([0,1,1,0,0,1,0,0],dtype=bool);
y = a[mask];
print(y);

#############################
#Fancy Indexing 2D
#############################
a = N.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]]);
print(a);
print(a[(0,1,2,3,4),(1,2,3,4,5)]);
print(a[3:,[0, 2, 5]]);
mask = N.array([1,0,1,0,0,1], dtype=bool);
print(a[mask,2]);

#############################
#Data-type fields
#############################

dt = N.dtype("i4,f8,a5")
print (dt.fields);

a = N.array([(1,2.0,'Hello'), (2,3.0,'World')], dtype=dt)
print(a);
print (a['f2']);

#############################
#Array Calculation Methods
#############################

#SUM FUNCTION
a = N.array([[1,2,3], [4,5,6]], float);

# Sum defaults to summing all
# *all* array values.
print( a.sum(axis=None));
print( a.sum(axis=0));
print( a.sum(axis=1));

#PRODUCT
print( a.prod(axis=None));
print( a.prod(axis=0));
print( a.prod(axis=1));

#MIN
print( a.min(axis=None));
print( a.min(axis=0));
print( a.min(axis=1));


#MAX
print( a.max(axis=None));
print( a.max(axis=0));
print( a.max(axis=1));

#ARGMIN
print( a.argmin(axis=None));
print( a.argmin(axis=0));
print( a.argmin(axis=1));

#ARGMAX
print( a.argmax(axis=None));
print( a.argmax(axis=0));
print( a.argmax(axis=1));

#############################
#Broadcasting
#############################
x = [1,2,3,4];
y = [[10],[20],[30]]

print (N.add(x,y));

#############################
#############################
# A INVESTIGAR
#############################
#############################

#############################
# Dot product of two arrays
#############################
a = N.array([[1, 0], [0, 1]]);
b = N.array([[4, 1], [2, 2]]);
c=N.dot(a, b)
print(a);
print(b);
print('----------------------');
print(c);

c=a @ b;
print(a);
print(b);
print('----------------------');
print(c);

#############################
# Determinante
#############################
a = N.array([[2,3,2],[1,2,1],[3,1,2]]);
print(a);
print('----------------------');
print(N.linalg.det(a))

#############################
# Rango de una matriz
#############################
print (N.linalg.matrix_rank(a));


#############################
# Moda de una matriz
#############################
print(st.mode(a));
print(st.mode(a).mode);


#############################
# Inversa de una matriz
#############################
inv_a=N.linalg.inv(a);
print (inv_a);

#############################
# Multiplicación de matrices
#############################
mult_a_inv=N.matmul(a,inv_a);

print(mult_a_inv);



###########################################################
# Solución de un sistema de ecuaciones (solución matricial)
###########################################################
# Matriz de coeficientes
A = N.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])

# Matriz de resultados
B = N.array([25, -10, -4])

# Resolviendo sistema de ecuaciones
X = N.linalg.inv(A).dot(B)

# Comprobando la solucion
print(A @ X == B)


# Usando Solve
X2 = N.linalg.solve(A,B)

# Comprobando la solucion
print(A @ X2 == B)





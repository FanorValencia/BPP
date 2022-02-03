row = 8
cols = 4

matriz = []

for i in range (row):
    r =[]
    for j in range (cols):
        r.append(i*cols+j)
    matriz.append(r)
#print (matriz)

m2 = [[i*cols+j for j in range (cols)] for i in range (row)]
print (m2)

def maximo (lista):
    return max(lista)

elem_maximos = list(map(maximo,m2))

print ('Los elementos mayores son: ', elem_maximos)

def primo(n):
    for i in range (2,n):
        if (n%i == 0):
            return False
    return True

num_primos = list(filter(primo,elem_maximos))

print ('Los primos son: ', num_primos)

def suma (a,b):
    return a+b

from functools import reduce
resultado_suma = reduce(suma,num_primos)

print ('La suma de los primos es: ', resultado_suma)
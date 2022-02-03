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
matriz = []
maior = 0
for i in range(3):
    tempLista = []
    for j in range(3):
        n = int(input())
        tempLista.append(n)
        if maior < n:
            maior = n
    matriz.append(tempLista)

for i in range(3):
    for j in range(3):
        if matriz[i][j] == maior:
            matriz[i][j] = -1
        
for i in range(3):
    for j in range(3):
        print(matriz[i][j] ,end=" ")
    print()
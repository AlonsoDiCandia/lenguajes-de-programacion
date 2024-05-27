dimesion = int(input("Ingrese un numero: "))

matriz = []

for i in range(dimesion):
    row = []
    for j in range(dimesion):
        row.append(0)
    matriz.append(row)

def imprimir_matriz(matriz):
    for row in matriz:
        print(' ', end='')
        for col in row:
            print(f"{col} ", end='')
        print()


for i in range(dimesion):
    for j in range(dimesion):
        if i == j:
            matriz[i][j] = 1
            
imprimir_matriz(matriz)


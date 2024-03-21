print(f"{'#'*15} Clase 0 {'#'*15}")

# Definimos la funcion que imprime
def imprimir_matriz(matriz):
    for row in matriz:
        print(' ', end='')
        for col in row:
            print(f"{col} ", end='')
        print()
    print(f"{(dimension*2+1)*'-'}")

while True:
    try: # Usamos un try para evitar que nuestro codigo se rompa si el usuario ingreso algo diferente a un numero. Si no entiende su funcion en este extracto de codigo, comentelo y pruebe ingresando en el input su nombre o un caracter no numerico.
        dimension = int(input("Ingrese un numero impar mayor que 0: "))
        if dimension > 0 and dimension % 2 == 1:
            break # Rompemos el bloque while para continuar con la matriz
    except: # Esto puede mejorar?
        print("Verifique que el numero sea impar y a la vez mayor que 0")

matriz = []

for i in range(dimension):
    row = []
    for j in range(dimension):
        row.append(0)
    matriz.append(row)

# Se imprime la matriz llena de ceros
imprimir_matriz(matriz)

# Buscamos las diagonales
# Debo recorrer toda la matriz para buscar las diagonales ?

for i in range(dimension):
    matriz[i][i] = 1
    matriz[i][dimension - i - 1] = 1

imprimir_matriz(matriz)

# De la misma forma podemos rellenar el contorno 
matriz[0][:] = [8 if matriz[0][i] != 1 else matriz[0][i] for i in range(dimension)]
matriz[dimension - 1][:] = [8 if matriz[dimension - 1][i] != 1 else matriz[dimension - 1][i] for i in range(dimension)]

for row in matriz:
    row[0] = 8 if row[0] != 1 else row[0]
    row[dimension - 1] = 8 if row[dimension - 1] != 1 else row[dimension - 1]

imprimir_matriz(matriz)

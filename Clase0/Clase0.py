print(f"{'#'*15} Clase 0 {'#'*15}")

# Definimos la funcion que imprime
def imprimir_matriz(matriz):
    for row in matriz:
        print(' ', end='')
        for col in row:
            print(f"{col} ", end='')
        print()
    print(f"{(dimension*2+1)*'-'}")

def rellenar_contorno(matriz, N, character):
    # matriz: Matriz con la que se va a trabajar, debe ser cuadrada, no se verifica esto ultimo, por favor asegurar esto o de lo contrario obtendra un error de indice probablemente.
    # N: hace referencia al contorno que se rellenara dado la matriz NxN que produzca. Ejemplo: Si N=5 y la matriz es de 9x9, esta funcion rellenara el contorno de la matriz 5x5 que este dentro de la matriz 9x9.
    
    dimension_matriz = len(matriz)
    diff_dimension = (dimension_matriz - N) // 2

    for e,row in enumerate(matriz):
        if e == diff_dimension or e == (dimension_matriz - diff_dimension - 1):
            for i in range(diff_dimension, dimension_matriz - diff_dimension):
                row[i] = character if row[i] != 1 else row[i]

        if e >= diff_dimension and (dimension_matriz - diff_dimension - 1) >= e:
            row[diff_dimension] = character if row[diff_dimension] != 1 else row[diff_dimension]
            row[dimension_matriz - diff_dimension - 1] = character if row[dimension_matriz - diff_dimension - 1] != 1 else row[dimension_matriz - diff_dimension - 1]

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
rellenar_contorno(matriz, 9, 8)
imprimir_matriz(matriz)
rellenar_contorno(matriz, 7, input("Ingrese un caracter: "))
imprimir_matriz(matriz)

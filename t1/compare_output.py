# Abre los dos archivos en modo de lectura
iguales = 0
with open('output.txt', 'r') as file1, open('output.txt', 'r') as file2:
    # Iterar sobre las líneas de ambos archivos
    for line1, line2 in zip(file1, file2):
        # Comparar las líneas
        if line1 == line2:
            iguales += 1
file1.close()
file2.close()

calculo = (iguales * 100) / 300

print(f'Nota propuesta: {calculo}')
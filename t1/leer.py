# Nombre del archivo a leer
nombre_archivo = '/Users/alonsodicandia/UFSM/ICI2/t1/caracteres.txt'
output = '/Users/alonsodicandia/UFSM/ICI2/t1/output.txt'

# Abrir el archivo en modo de lectura
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    # Leer cada línea del archivo
    selection_p1 = 1 #int(input('Seleccione que respuesta quiere probar para la pregunta 1 (1, 2 o 3): '))
    for linea in archivo:
        print(linea)
        # primer print hace referencia a el conteo de caracteres, las opciones para responder esta pregunta son:
        
        if selection_p1 == 1:
                p1=0
                p1 = len(linea.strip()) 
        elif selection_p1 == 2:
            p1 = 0
            for caracter in linea:
                if caracter != ' ' and caracter != '\n':
                    p1 += 1
        elif selection_p1 == 3:
            p1 = 0
            no_se_cuentan = [' ', '\n']
            p1 = len([letra for letra in linea if letra not in no_se_cuentan])

        # Notar que las opciones 2 y 3 puedes ser permutadas, es decir el bloque if puede contar con la lista o la lista en una linea puede tener dos condiciones

        # Pregunta 2
        p2 = 0
        vocales = ['a', 'e', 'i', 'o', 'u']
        for letra in linea:
            if letra in vocales:
                p2 += 1      
        
        p3 = -100
        for letra in linea:
            if ord(letra) > p3:
                p3 = ord(letra)

        p4 = ''
        list_p4 = []
        for letra in linea:
            if letra not in vocales and letra not in [' ', '\n']:
                list_p4.append(str(ord(letra.upper())))
        p4 = ''.join(list_p4)

        with open(output, 'a', encoding='utf-8') as ouput_file:
            ouput_file.write(f'{p1} {p2} {p3} {p4} \n')

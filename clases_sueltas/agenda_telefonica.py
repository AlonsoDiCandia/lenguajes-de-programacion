def cerrar_ciclo(var):
    # var debe ser de tipo booleano
    return not var

def agregar_persona():
    rut = input('Ingrese su rut: ')
    agenda_telefonica[rut] = {
        'nombre': input('Ingrese su nombre: '),
        'apellido': input('Ingrese su apellido: '),
        'telefono': input('Ingrese su telefono: '),
        'signo': input('Ingrese su signo: ')
}

on_off = True
# {'18800994481': {'nombre': 'Alonso', 'apellido': 'Diaz', 'telefono': '45678', 'signo': 'Leo'}}
agenda_telefonica = {}

bienvenida = f'''{'#'*20} AGENDA TELEFONICA {'#'*20}
Escoja una opción de la siguiente lista:
1.- Agregar persona
0.- Cerrar agenda telefonica
'''
while on_off:
    
    print(bienvenida)
    
    try:
        user_option = int(input('Elija una opción: '))
        if user_option < 0:
            print('Por favor elija un numero mayor o igual que 0 :)')
            continue
    except:
        print('Por favor ingrese un numero :)')
        continue

    if user_option == 0:
        on_off = cerrar_ciclo(on_off)
    elif user_option == 1:
        agregar_persona()
        print(agenda_telefonica)

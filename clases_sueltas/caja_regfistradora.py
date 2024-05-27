import random

def cerrar_ciclo(var):
    # var debe ser de tipo booleano
    return not var

productos = {
    '1': {
        'tipo': 'galletas',
        'sku': '1245673891203',
        'fecha de expiracion': '03/06/2024'
    },
    '2': {
        'tipo': 'chocolate',
        'sku': '2345678891203',
        'fecha de expiracion': '04/06/2024'
    },
    '3': {
        'tipo': 'mani',
        'sku': '3345673891203',
        'fecha de expiracion': '05/06/2024'
    },
    '4': {
        'tipo': 'pan',
        'sku': '4345673891203',
        'fecha de expiracion': '06/06/2024'
    },
    '5': {
        'tipo': 'queso',
        'sku': '5345673891203',
        'fecha de expiracion': '07/06/2024'
    },
    '6': {
        'tipo': 'tomate',
        'sku': '6345673891203',
        'fecha de expiracion': '08/06/2024'
    },
    '7': {
        'tipo': 'fideos',
        'sku': '7345673891203',
        'fecha de expiracion': '09/06/2024'
    },
    '8': {
        'tipo': 'not mayo',
        'sku': '8345673891203',
        'fecha de expiracion': '10/06/2024'
    },
    '9': {
        'tipo': 'doritos',
        'sku': '9345673891203',
        'fecha de expiracion': '11/06/2024'
    },
    '10': {
        'tipo': 'coca cola',
        'sku': '10345673891203',
        'fecha de expiracion': '12/06/2024'
    },
    '11': {
        'tipo': 'redbull',
        'sku': '11345673891203',
        'fecha de expiracion': '13/06/2024'
    },
    '12': {
        'tipo': 'mate',
        'sku': '12345673891203',
        'fecha de expiracion': '14/06/2024'
    },
    '13': {
        'tipo': 'cafe',
        'sku': '13345673891203',
        'fecha de expiracion': '15/06/2024'
    },
    '14': {
        'tipo': 'manjar',
        'sku': '14345673891203',
        'fecha de expiracion': '16/06/2024'
    },
    '15': {
        'tipo': 'not leche',
        'sku': '15345673891203',
        'fecha de expiracion': '17/06/2024'
    }
}

on_off = True

for key, value in productos.items():
    value['coste'] = random.randint(1500, 20000)
    print(f"{key}.-\t{value['tipo']}\t${value['coste']}\t{value['fecha de expiracion']}")


carrito = []

while on_off:
    try:
        producto_escogido = input('Elija una opción: ')
        if producto_escogido in productos.keys():
            carrito.append(productos[producto_escogido])
    except Exception as e:
        print('Por favor ingrese un producto valido.')
        continue

    for item in carrito:
        print(item)
    

    if producto_escogido == 'salir':
        on_off = cerrar_ciclo(on_off)
    elif producto_escogido == 'carrito':
        print(carrito)
    elif producto_escogido == 'total':
        total = sum(list(map(lambda x: x['coste'], carrito)))
        print(f'El total es {total}')

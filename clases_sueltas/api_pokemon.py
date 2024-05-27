import requests
import time

def obtener_datos_de_api(url):
    # Realiza una petición GET a la URL proporcionada
    response = requests.get(url)

    # Verifica que la petición se haya realizado correctamente
    if response.status_code == 200:
        try:
            # Intenta convertir la respuesta JSON en una lista de diccionarios
            data = response.json()
            return data
        except ValueError:
            # Maneja el caso donde la respuesta no es un JSON válido
            print("Error: No se pudo decodificar el JSON")
    else:
        # Imprime el código de estado HTTP si la petición no fue exitosa
        print(f"Error: La petición HTTP falló con el código {response.status_code}")

# URL de la API
url_api = 'https://pokeapi.co/api/v2/pokemon?limit=151'
# 'https://pokeapi.co/api/v2/pokemon/1'

# Obtiene los datos de la API
datos_recibidos = obtener_datos_de_api(url_api)

# pokemons = datos_recibidos['results']

# Imprime los datos recibidos
# print(datos_recibidos)

pokemons = datos_recibidos['results']
types = {}

print(pokemons)
for pokemon in pokemons:
    poke_data = obtener_datos_de_api(pokemon['url'])
    tipos = poke_data['types']
    for tipo in tipos:
        foo = tipo['type']['name']
        if foo in types.keys():
            types[foo] += 1
        else:
            types[foo] = 1
print(types)

atacks = {}

for pokemon in pokemons:
    poke_data = obtener_datos_de_api(pokemon['url'])
    moves = poke_data['moves']
    for move in moves:
        foo = move['move']['name']
        if foo in atacks.keys():
            atacks[foo] += 1
        else:
            atacks[foo] = 1

print(atacks)
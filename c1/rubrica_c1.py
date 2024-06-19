import json
import random 

# Abriendo un archivo JSON desde el sistema de archivos
with open('c1/clash_royale.json', 
'r') as archivo:
    datos = json.load(archivo)

# Ahora `datos` es un diccionario de Python con los datos del archivo JSON

def get_random_rarity():
    rarity = [
        'common',
        'rare',
        'epic', 
        'legendary'
    ]

    return random.choice(rarity)

def create_card(card='New card'):
    card = {
        'name': card, 
        'id': random.randint(28000000,29000000), 
        'maxLevel': random.randint(1,15), 
        'elixirCost': random.randint(1,11), 
        'rarity': get_random_rarity()
    }

    return(card)

spaces = 0
types = dict()
mega_evolution = 0

for card in datos['items']:
    print(card)
    spaces += card['name'].count(' ')

    rarity = card['rarity']

    if rarity in types.keys():
        types[rarity] += 1
    else:
        types[rarity] = 1
    
    if 'maxEvolutionLevel' in card.keys():
        mega_evolution += 1

    

print(len(datos['items']))
print(spaces)
print(types)
print(mega_evolution)

print(create_card())

############### BONUS ###############

# Habian varias formas de hacer el bonus, algunas son: crear una lista de nombres a mano, traer los nombres de una api, generar un nombre con caracteres aleatorios (nunca se dijo que debia tener sentido el nombre, no era un requerimiento)
# Veremos la de crear algo a mano

nombres = ["Conga", "Guau", "Ringo", "Bingo", "Fido", "Bobby", "Chicho", "Pepe", "Nero", "Blackie", "Lady"]

print(create_card(random.choice(nombres)))


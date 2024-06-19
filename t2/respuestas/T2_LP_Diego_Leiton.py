import requests
import math
import random
from random import choice

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
url_api = 'https://pokeapi.co/api/v2/pokemon?limit=1025' #'https://pokeapi.co/api/v2/pokemon?limit=151'

# Obtiene los datos de la API
datos_recibidos = obtener_datos_de_api(url_api)

pokemon_data=datos_recibidos['results']

nombre_pokemon=[]

for pokemon in pokemon_data:
    nombre_pokemon.append(pokemon['name'])


#1 Crear clase criatura, atributos vida, ataque y defensa
#se debe tener métodos para poder modificar los atributos


#2 Cada criatura deberá tener un nombre pasado como parametro
#en su creacion; sobrecargar el métodod para que al hacer print
#se imprima el nombre de la criatura mas no el objeto


#usando la clase creada en el punto 1 crear una lista de criaturas
#8 objetos criatura deben ser creados y agregados a la lista
#BONUS: CREAR n criaturas donde n es una potencia de 2


class Pokemon:
    def __init__(self,nombre):
        self.nombre = nombre
        self.ataque = random.randint(1,10)
        self.defensa = random.randint(1,5)
        self.vida= random.randint(20,120)
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return self.__str__()
    
    def get_info(self):
        return (f'Nombre pokemon: {self.nombre}, Ataque Pokemon: {self.ataque}, Defensa pokemon: {self.defensa}, HP: {self.vida}')
    
    def hp_actual(self,damage):
        self.vida -= damage
        if self.vida <= 0:
            self.vida=0
        return self.vida
    
    def restaurar_hp(self):
        self.vida = 120
        return self.vida
    
    
lista_pokemon=[]

#termine haciendo una función para tener el rango de criaturas que deseo tener, donde use logaritmo de base 2
#ya que el logaritmo es la función inversa de las potencias

def rango_potencia_2():
    while True:
        rango= int(input("Ingrese la cantidad de pokemones que desea hacer participar en el torneo: "))
        if rango <= 0:
            print("Por favor, ingresa un número positivo.")
            continue

        flag= math.log2(rango)
        if flag.is_integer():
            print(f'{rango} es una potencia de 2.')
            return rango
        else:
            print(f'{rango} no es una potencia de 2. Intente denuevo')

rango = rango_potencia_2()
print(f'El total de pokemons elegidos es: {rango}')

for _ in range(rango):
    name_aleatorio= random.choice(nombre_pokemon)
    nombre_pokemon.remove(name_aleatorio)
    p= Pokemon(name_aleatorio)
    lista_pokemon.append(p)

    #print(p.get_info()) #Nombre pokemon: rhydon, Ataque Pokemon: 8, Defensa pokemon: 5, HP: 100 

def combates(pokemon1,pokemon2):
    damage1 = max(0,pokemon1.ataque - pokemon2.defensa)
    damage2 = max(0,pokemon2.ataque - pokemon1.defensa)
    pokemon1.restaurar_hp()
    pokemon2.restaurar_hp()

    if damage1 == 0:
        print(f'dado que {pokemon1} no es capaz de realizar daño a {pokemon2}, este ultimo pasa de ronda')
        return pokemon2
    elif damage2 ==0:
        print(f'dado que {pokemon2} no es capaz de realizar daño a {pokemon1}, este ultimo pasa de ronda')
        return pokemon1
    else:
        while pokemon1.vida > 0 and pokemon2.vida > 0:
            pokemon1.hp_actual(damage2)
            pokemon2.hp_actual(damage1)
            #print(f'{pokemon1} ataca a pokemon {pokemon2}, quitando {damage1} de hp. {pokemon2} tiene: {pokemon2.vida} de hp')
            #print(f'{pokemon2} ataca a pokemon {pokemon1}, quitando {damage2} de hp. {pokemon1} tiene: {pokemon1.vida} de hp')
        if pokemon1.vida == 0 and pokemon2.vida == 0:
            print('ocurrio un empate por lo que el ganador se elegira al azar')
            return random.choice([pokemon1,pokemon2])       
        elif pokemon1.vida == 0:
            print(f'{pokemon2} ha abatido a {pokemon1}, quitando {damage2} de hp. {pokemon2} pasa con: {pokemon2.vida} de hp')
            return pokemon2
        elif pokemon2.vida == 0:
            print(f'{pokemon1} ha abatido a pokemon {pokemon2}, quitando {damage1} de hp. {pokemon1} pasa con: {pokemon1.vida} de hp')
            return pokemon1



def torneo(lista, ronda):
    #largo_lista=len(lista)
    print(comentario_2)
    for i in range(ronda):
        ganadores=[]
        print(f'Ronda: {i+1}, participan {lista}')
        while len(lista) > 1:
            pokemon1 = random.choice(lista)
            lista.remove(pokemon1)
            pokemon2 = random.choice(lista)
            lista.remove(pokemon2)
            ganador = combates(pokemon1,pokemon2)
            print(f'Combate: {pokemon1} vs {pokemon2} - Ganador: {ganador}')
            #largo_lista = len(lista) #actualizar el largo
            ganadores.append(ganador)
        lista=ganadores
        print(f'Quienes continuan a la ronda siguiente son {lista} ')

    return ganadores[0]

def combate_round_robin(pokemon1,pokemon2):
    damage1 = max(0,pokemon1.ataque - pokemon2.defensa)
    damage2 = max(0,pokemon2.ataque - pokemon1.defensa)
    pokemon1.restaurar_hp()
    pokemon2.restaurar_hp()

    if damage1 == 0:
        print(f'dado que {pokemon1} no es capaz de realizar daño a {pokemon2}. este ultimo gana +3 ptos')
        return pokemon2,3
    elif damage2 == 0:
        print(f'dado que {pokemon2} no es capaz de realizar daño a {pokemon1}. este ultimo gana +3 ptos')
        return pokemon1,3
    else:
        while pokemon1.vida and pokemon2.vida > 0:
            pokemon1.hp_actual(damage2)
            pokemon2.hp_actual(damage1)

        if pokemon1.vida == 0 and pokemon2.vida == 0:
            print(f'ha habido un empate: {pokemon1} y {pokemon2} +1 pto')
            return None,1
    
        elif pokemon1.vida == 0:
            print(f'{pokemon2} ha abatido a {pokemon1}. {pokemon2} +3 ptos')
            return pokemon2,3
    
        elif pokemon2.vida == 0:
            print(f'{pokemon1} ha abatido a {pokemon2}. {pokemon1} +3 ptos')
            return pokemon1,3
        

def torneo_todos_vs_todos(lista,rango):
    print(comentario_1)
    puntos={pokemon: 0 for pokemon in lista} #con este for recorro la lista y creo las llaves y valores de puntos
    i=0
    for pokemon in lista:
        i+=1
        for x in range(i,rango):
            if pokemon == lista[x]:
                continue
            winner, point = combate_round_robin(pokemon,lista[x])
            if winner is None:
                puntos[pokemon] += 1
                puntos[lista[x]] +=1     
            else:
                puntos[winner] += point
    tabla_ordenada= sorted(puntos.items (), key=lambda x:x[1], reverse=True)
    return tabla_ordenada

rondas= int(math.log2(rango)) #para definir las rondas se me ocurrio usar el mismo logaritmo base 2 por pura matematica


comentario_1=''' 
--------------------------------------------------------------------
TORNEO TODOS VS TODOS
--------------------------------------------------------------------
'''

comentario_2=''' 
--------------------------------------------------------------------
TORNEO POR LLAVES
--------------------------------------------------------------------
'''


ganador_todos_vs_todos = torneo_todos_vs_todos(lista_pokemon,rango)
print(f'En el todos contra todos la tabla de puntos es la siguiente: {ganador_todos_vs_todos}')
print('\n')


ganador_bracket=torneo(lista_pokemon,rondas)

#print("soy la lista de pokemones",lista_pokemon)

print(f'El ganador del torneo es: {ganador_bracket}')
print('\n')




'''
la idea de mi codigo era generar algo capaz que con pocas modificaciones permita tomar mayor cantidad de datos, dado que mientras haya
cadenas de texto ordenadas en una lista se podra hacer objeto y darle atributos para hacer un bracket de torneo, en el caso de pokemon
hay los suficientes para que el codigo funcione hasta la potencia de 2 elevado a 10, es decir 1024 pokemones cambiando la url
a https://pokeapi.co/api/v2/pokemon?limit=1025 , ademas podria servir para tomar nombres de otras apis de internet o de bases de datos dado
que esta implementado en conjunto al codigo de request de la tarea 1

en cuanto a los formatos decidi usar en el de por llaves un formato en el que sea aleatorio los brackets

'''



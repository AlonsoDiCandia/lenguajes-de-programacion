'''
Favor, para hacer las consultas de las funciones, utilizar de manera individual, no ambas juntas.
Se crea un error que no pude solucionar, pero funcionan individualmente.
Saludos.-
'''

import random

nombres = [
    "Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol",
    "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath",
    "Corki", "Darius", "Diana", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks",
    "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger",
    "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista",
    "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled"
]

class Criatura:
    def __init__(self, nombre, vida, ataque, defensa):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    def get_nombre(self):
        return self.__nombre

    def get_vida(self):
        return self.__vida

    def get_ataque(self):
        return self.__ataque

    def get_defensa(self):
        return self.__defensa

    def set_vida(self, vida):
        self.__vida = vida

    def set_ataque(self, ataque):
        self.__ataque = ataque

    def set_defensa(self, defensa):
        self.__defensa = defensa

    def __str__(self):
        return self.__nombre

def generar_criaturas(nombres):
    criaturas = []
    for nombre in nombres:
        vida = random.randint(50, 100)
        ataque = random.randint(10, 20)
        defensa = random.randint(5, 15)
        criatura = Criatura(nombre, vida, ataque, defensa)
        criaturas.append(criatura)
    return criaturas

def combate(criatura1, criatura2):
    dano1 = max(0, criatura1.get_ataque() - criatura2.get_defensa())
    dano2 = max(0, criatura2.get_ataque() - criatura1.get_defensa())

    vida1 = criatura1.get_vida() - dano2
    vida2 = criatura2.get_vida() - dano1

    if vida1 > vida2:
        return criatura1
    elif vida2 > vida1:
        return criatura2
    else:
        return None  # Indica un empate

def eliminacion_directa_con_rondas(criaturas):
    rondas = []
    while len(criaturas) > 1:
        ronda_actual = []
        ganadores = []
        for i in range(0, len(criaturas) - 1, 2):
            ganador = combate(criaturas[i], criaturas[i + 1])
            if ganador is not None:
                ronda_actual.append(f"{criaturas[i].get_nombre()} vs {criaturas[i + 1].get_nombre()} -> el ganador es: {ganador.get_nombre()}")
                ganadores.append(ganador)
            else:
                print('empate'*15)
        if len(criaturas) % 2 == 1:
            ganadores.append(criaturas[-1])
        rondas.append(ronda_actual)
        criaturas = ganadores
    return criaturas[0], rondas

criaturas = generar_criaturas(nombres)
ganador, rondas = eliminacion_directa_con_rondas(criaturas)

print("Llaves del torneo:")
for i, ronda in enumerate(rondas):
    print(f"Ronda {i + 1}:")
    for combate in ronda:
        print(combate)
print(f"La criatura ganadora es: {ganador.get_nombre()}")

'''
def sistema_todos_contra_todos(criaturas):
    puntuaciones = {criatura.get_nombre(): 0 for criatura in criaturas} 
    
    for i in range(len(criaturas)): 
        for j in range(i + 1, len(criaturas)):  
            resultado = combate(criaturas[i], criaturas[j]) 
            if resultado is None:
                puntuaciones[criaturas[i].get_nombre()] += 1 
                puntuaciones[criaturas[j].get_nombre()] += 1
            elif resultado == criaturas[i]:
                puntuaciones[criaturas[i].get_nombre()] += 3 
            else:
                puntuaciones[criaturas[j].get_nombre()] += 3

    return puntuaciones

criaturas = generar_criaturas(nombres)
puntuaciones = sistema_todos_contra_todos(criaturas)

print("Puntuaciones del sistema todos contra todos:")
for nombre, puntuacion in puntuaciones.items():
    print(f"{nombre}: {puntuacion} puntos")
'''

## Rodrigo Lopez Ponce ###
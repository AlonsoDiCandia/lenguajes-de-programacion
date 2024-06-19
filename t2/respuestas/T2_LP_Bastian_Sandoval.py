
import random
from itertools import combinations

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

def combate(criatura1, criatura2):
    score1 = criatura1.get_ataque() - criatura2.get_defensa()
    score2 = criatura2.get_ataque() - criatura1.get_defensa()
    
    if score1 > score2:
        return criatura1
    elif score2 > score1:
        return criatura2
    else:
        return random.choice([criatura1, criatura2])

def torneo(criaturas):
    ronda = 1
    while len(criaturas) > 1:
        print(f'Ronda {ronda}:')
        next_round = []
        for i in range(0, len(criaturas), 2):
            ganador = combate(criaturas[i], criaturas[i+1])
            next_round.append(ganador)
            print(f'{criaturas[i]} vs {criaturas[i+1]} -> {ganador} gana')
        criaturas = next_round
        ronda += 1
    return criaturas[0]

def todos_contra_todos(criaturas):
    puntos={}
    for criatura in criaturas:
        puntos[criatura]=0
    
    
    for criatura1, criatura2 in combinations(criaturas, 2):
        ganador = combate(criatura1, criatura2)
        if ganador:
            puntos[ganador] += 3
        else:
            puntos[criatura1] += 1
            puntos[criatura2] += 1
    
    return puntos

# Función para generar valores aleatorios para los atributos
def generar_atributos():
    vida = random.randint(80, 120)
    ataque = random.randint(20, 40)
    defensa = random.randint(15, 35)
    return vida, ataque, defensa

# Crear las criaturas 
nombres = ["Python", "Java", "PHP", "C++", "Swift", "R", "Kotlin", "Assembly"]

criaturas = []
for nombre in nombres:
    atributos = generar_atributos()
    criatura = Criatura(nombre, atributos[0], atributos[1], atributos[2])
    criaturas.append(criatura)

from matplotlib import pyplot as plt
x = [foo.get_nombre() for foo in criaturas]
y = [foo.get_ataque() for foo in criaturas]
print(f'El promedio de ataque es: {sum(y)/len(y)}')

plt.figure(1)
plt.plot(x, y)
plt.show()


# Iniciar el torneo y mostrar al campeón
print("Torneo estilo llaves:")
campeon = torneo(criaturas)
print(f'El campeón es {campeon}!')

# Mostrar resultados del todos contra todos
print("\nSistema todos contra todos:")
puntos = todos_contra_todos(criaturas)
sorted_puntos = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
for criatura, puntos in sorted_puntos:
    print(f'{criatura}: {puntos} puntos')

import random

def combate(luchador1, luchador2):
    registro = []
    while luchador1.obtener_vida() > 0 and luchador2.obtener_vida() > 0:
        daño1 = max(luchador1.obtener_ataque() - luchador2.obtener_defensa(), 0)
        luchador2.modificar_vida(luchador2.obtener_vida() - daño1)
        registro.append(f"{luchador1} ataca a {luchador2} y causa {daño1} de daño.")
        
        if luchador2.obtener_vida() <= 0:
            registro.append(f"{luchador1} gana el combate.")
            break
        
        daño2 = max(luchador2.obtener_ataque() - luchador1.obtener_defensa(), 0)
        luchador1.modificar_vida(luchador1.obtener_vida() - daño2)
        registro.append(f"{luchador2} ataca a {luchador1} y causa {daño2} de daño.")
        
        if luchador1.obtener_vida() <= 0:
            registro.append(f"{luchador2} gana el combate.")
            break
    
    ganador = luchador1 if luchador1.obtener_vida() > 0 else luchador2
    return ganador, registro

def torneo(luchadores):
    registros = []
    ronda = 1
    while len(luchadores) > 1:
        random.shuffle(luchadores) 
        ganadores = []
        for i in range(0, len(luchadores), 2):
            ganador, registro = combate(luchadores[i], luchadores[i + 1])
            registros.append((ronda, registro))
            ganadores.append(ganador)
        luchadores = ganadores
        ronda += 1
    return luchadores[0], registros

class uFcFighter:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__vida = random.randint(50, 200)
        self.__ataque = random.randint(10, 50)
        self.__defensa = random.randint(5, 25)
    
    def modificar_vida(self, vida):
        self.__vida = vida
    
    def modificar_ataque(self, ataque):
        self.__ataque = ataque
    
    def modificar_defensa(self, defensa):
        self.__defensa = defensa
    
    def obtener_vida(self):
        return self.__vida
    
    def obtener_ataque(self):
        return self.__ataque
    
    def obtener_defensa(self):
        return self.__defensa
    
    def __str__(self):
        return self.__nombre

nombresLuchadores = [
    'Dustin Poirier', 'Islam Makhachev',
    'Khabib Nurmagomedov', 'Conor McGregor',
    'Charles Oliveira', 'Alexander Volkanovski',
    'Justin Gaethje', 'Ilia Topuria'
]

luchadores = [uFcFighter(nombre) for nombre in nombresLuchadores]

campeon, registros = torneo(luchadores)

for ronda, registro in registros:
    print(f"\nRonda {ronda}:")
    for evento in registro:
        print(evento)

print(f"\nEl campeon de las 155LB del peso ligero de la UFC es: {campeon}")        
import random
import sys
import time

def CuarzoPapiroNavaja(x, y):
    if x==1:
        return 1
    if x == y:
        return 0
    elif (x == 'cuarzo' and y == 'navaja') or \
         (x == 'navaja' and y == 'papiro') or \
         (x == 'papiro' and y == 'cuarzo'):
        return 1
    else:
        return 2

class Criatura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(1, 10)
        self.ataque = random.randint(1, 10)
        self.defensa = random.randint(1, 10)
        self.puntos = 0

    def modificar_atributos(self, vida, ataque, defensa):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
    
    def __str__(self):
        return (f"{self.nombre}: Vida={self.vida}, Ataque={self.ataque}, "
                f"Defensa={self.defensa}, Puntos={self.puntos}")

def combate(criatura1, criatura2):
    turno = random.choice([1, 2])
    time.sleep(1)
    print(f"Se pillaron de frente {criatura1.nombre} y {criatura2.nombre}")
    while criatura1.vida > 0 and criatura2.vida > 0:
        if turno == 1:
            vida_aux = (criatura2.vida + criatura2.defensa) - criatura1.ataque
            criatura2.vida = vida_aux
            criatura2.defensa //= 2
            turno = 2
            time.sleep(1.5)
            print(f"{criatura1.nombre} ataca con {criatura1.ataque} a {criatura2.nombre}")
            print(f"{criatura2.nombre} ha quedado con {vida_aux} de vida")
            time.sleep(1.5)
        else:
            vida_aux = (criatura1.vida + criatura1.defensa) - criatura2.ataque
            criatura1.vida = vida_aux
            criatura1.defensa //= 2
            turno = 1
            print(f"{criatura2.nombre} ataca con {criatura2.ataque} a {criatura1.nombre}\n"
                  f"{criatura1.nombre} ha quedado con {vida_aux} de vida")
            time.sleep(1.5)

    if criatura1.vida > 0:
        criatura1.puntos+= 3
        return criatura1, criatura2
    else:
        criatura2.puntos+= 3
        return criatura2, criatura1

def jugar_ronda(orden_torneo, character, elecciones, espectador):
    ganadores = []
    for c in orden_torneo:
        jugador1 = c[0]
        jugador2 = c[1]
        if espectador:
            time.sleep(1)
            print(f'Los participantes {jugador1} y {jugador2} se van a enfrentar')
        while True:
            if jugador1 == character:
                eleccion1 = input(f'{jugador1}, elige cuarzo, papiro o navaja: ').lower()
                while eleccion1 not in elecciones:
                    eleccion1 = input(f'Error, {jugador1}, elige una opción correcta: cuarzo, papiro o navaja: ').lower()
            else:
                eleccion1 = random.choice(elecciones)
            if jugador2 == character:
                eleccion2 = input(f'{jugador2}, elige cuarzo, papiro o navaja: ').lower()
                while eleccion2 not in elecciones:
                    eleccion2 = input(f'Error, {jugador2}, elige una opción correcta: cuarzo, papiro o navaja: ').lower()
            else:
                eleccion2 = random.choice(elecciones)
            resultado = CuarzoPapiroNavaja(eleccion1, eleccion2)
            if espectador:
                time.sleep(1)
                print(f'{jugador1} elige {eleccion1} y {jugador2} elige {eleccion2}')
            if resultado != 0:
                break
            if espectador or jugador1 == character or jugador2 == character:
                print("¡Hubo un empate! Vuelven a elegir.")
        ganador = jugador1 if resultado == 1 else jugador2
        if espectador:
            time.sleep(1)
            print(f'El ganador fue {ganador}')
        ganadores.append(ganador)
    return ganadores

def ffa_torneo(criaturas):
    while len(criaturas) > 1:
        cri1, cri2 = random.sample(criaturas, 2)
        ganador, perdedor = combate(cri1, cri2)
        time.sleep(1.5)
        print(f"\nGanador: {ganador.nombre}\n")
        criaturas.remove(perdedor)
        time.sleep(2)
        # Mostrar las stats de todas las criaturas después de cada pelea.
        for c in criaturas:
            print(c)
        time.sleep(3)
        print(f"\nPor otro lado del mapa....\n") if len(criaturas) > 1 else print(f"\nEl unico sobreviviente de esta masacre fue {criaturas[0].nombre}\n")

    ganador_final = criaturas[0]
    ganador_final.puntos += 3
    time.sleep(1)
    print(f"¡{ganador_final.nombre} ha ganado el modo FFA de el Torneo de Cell 2024!")

elecciones = ['cuarzo', 'papiro', 'navaja']
criaturas = []
nombres = ['Huevo Rey', 'Lad Cobra', 'Choche07', 'Rene Puente', 'Papi Micky', 'Ñanckson', 'Flaitiano', 'Corxea']

for _ in nombres:
    aux = Criatura(_)
    criaturas.append(aux)

print('Bienvenido a el Torneo de Cell 2024 \n¡Choice your character!\n')
for c in nombres:
    print(f'- {c}')

while True:
    character = input()
    if character not in nombres:
        print("¡Error! Ese personaje no existe en la versión 2024 de este juego.\n")
    else:
        break

for c in criaturas:
    if c.nombre == character:
        print(f"\nHas elegido a {character}, sus atributos son:\n"
              f"Vida: {c.vida}\n"
              f"Ataque: {c.ataque}\n"
              f"Defensa: {c.defensa}\n\n")
        print("Lamentablemente estos atributos no te servirán para nada, ya que todos\n"
              "van a competir en un torneo de Cuarzo, Papiro y Navaja.\n\n")
        print("(Los atributos servirán para el modo FFA, llega a la final o gana\n"
              "la partida para desbloquear este modo)\n")
        time.sleep(2)

input("¡Presiona 'Enter' para continuar!\n")

copia_nombres = nombres.copy()
distancia = len(nombres)
copia_nombres.remove(character)
orden_torneo = []
lista_aux = []
#Funcion que hace un orden random de los participantes del torneo
for j in range(distancia):
    if j == distancia - 1:
        lista_aux.append(character)
        orden_torneo.append(lista_aux)
        break
    aux = random.choice(copia_nombres)
    if len(lista_aux) < 2:
        lista_aux.append(aux)
    else:
        orden_torneo.append(lista_aux)
        lista_aux = []
        lista_aux.append(aux)
    copia_nombres.remove(aux)
print(f'El orden del torneo es el siguiente:\n\n'
      f'{orden_torneo[0][0]}\n vs\n'
      f'{orden_torneo[0][1]}\n\n'
      f'{orden_torneo[1][0]}\n vs\n'
      f'{orden_torneo[1][1]}\n\n'
      f'{orden_torneo[2][0]}\n vs\n'
      f'{orden_torneo[2][1]}\n\n'
      f'{orden_torneo[3][0]}\n vs\n'
      f'{orden_torneo[3][1]}')
time.sleep(3)
print('\n¡Los enfrentamientos van a comenzar!\n')
espectador = input("Si quieres ver los enfrentamientos presiona '0', de lo contrario presiona '1'\n")
espectador = True if espectador == '0' else False

# Primera ronda
ganadores_primera_ronda = jugar_ronda(orden_torneo, character, elecciones, espectador)

if character not in ganadores_primera_ronda:
    print(f'Te ha vencido {ganadores_primera_ronda[-1]}\n')
    print('Game Over!\n\nInsert a coin to play again ;)')
    sys.exit(0)
else:
    print(f'Ganadores de la primera ronda: ')
    for c in ganadores_primera_ronda:
        print(f'- {c}')

# Crear segunda lista
orden_torneo = []
aux = []
i = 0

while i < len(ganadores_primera_ronda):
    if len(aux) < 2:
        aux.append(ganadores_primera_ronda[i])
    if len(aux) == 2:
        orden_torneo.append(aux)
        aux = []
    i += 1

print('\n¡La segunda ronda va a comenzar!\n')
print(f'El orden del torneo es el siguiente:\n\n'
      f'{orden_torneo[0][0]}\n vs\n'
      f'{orden_torneo[0][1]}\n\n'
      f'{orden_torneo[1][0]}\n vs\n'
      f'{orden_torneo[1][1]}\n\n')

# Segunda ronda
ganadores_segunda_ronda = jugar_ronda(orden_torneo, character, elecciones, espectador)

if character not in ganadores_segunda_ronda:
    print(f'Te ha vencido {ganadores_segunda_ronda[-1]}\n')
    print('Game Over!\n\nInsert a coin to play again ;)')
    sys.exit(0)
else:
    print(f'Ganadores de la segunda ronda: ')
    for c in ganadores_segunda_ronda:
        print(f'- {c}')

# Crear tercera y ultima lista 
orden_torneo = []
aux = []
i = 0

while i < len(ganadores_segunda_ronda):
    if len(aux) < 2:
        aux.append(ganadores_segunda_ronda[i])
    if len(aux) == 2:
        orden_torneo.append(aux)
        aux = []
    i += 1

print('\n¡La final va a comenzar!\n')
print(f'El orden del torneo es el siguiente:\n\n'
      f'{orden_torneo[0][0]}\n vs\n'
      f'{orden_torneo[0][1]}\n\n')

# La gran final
ganador_final = jugar_ronda(orden_torneo, character, elecciones, espectador)

if character not in ganador_final:
    print(f'Te ha vencido {ganador_final[-1]}\n')
    print('Game Over!\n\nInsert a coin to play again ;)\n')
else:
    print(f'¡Felicidades! {ganador_final[0]} eres el campeón del Torneo de Cell 2024!\n')
time.sleep(1)
# ffa = input('Ahora se te da la oportunidad de participar en un FFA de todos contra todos...\n\n'
            # 'Presiona 0 si quieres participar, de lo contrario puedes apagar la consola.\n')

ffa = True #True if ffa == '0' else False

if ffa:
    print('¡Has empezado el modo FFA!')
    ffa_torneo(criaturas)

    while True:
        jugar_otra_vez = input('¿Quieres jugar otra vez? Presiona 0 para jugar de nuevo, cualquier otra tecla para salir: \n').lower()
        if jugar_otra_vez == '0':
            time.sleep(4)
            print('Se ha conseguido un barril de gas de Return of the Living Dead! Todos los jugadores han sido revividos!\n')
            #Se que puedo hacer una funcion para generar la lista de clases "Criaturas" automaticamente, pero llevo tantos dias con
            #tantos fallos y bugs que prefiero no tocar más el codigo.. y como dicen "Si funciona no lo toques" XD
            for _ in nombres:
                aux = Criatura(_)
                criaturas.append(aux)
            for criatura in criaturas:
                criatura.vida = random.randint(1, 10)
                criatura.ataque = random.randint(1, 10)
                criatura.defensa = random.randint(1, 10)
            ffa_torneo(criaturas)
        else:
            print('Gracias por jugar. *Apaga la consola*')
            break
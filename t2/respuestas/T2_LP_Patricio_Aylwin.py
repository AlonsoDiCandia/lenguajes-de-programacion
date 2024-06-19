import random

class Criatura:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.ataque = random.randint(10, 50)
        self.defensa = random.randint(1, 50)

    def __str__(self):
        return self.nombre

    def pelear(self, otro_jugador):
        # el daño efectivo que es el daño menos la defensa del otro (gracias yo del pasado)
        mi_ataque_efectivo = max(0, self.ataque - otro_jugador.defensa)
        otro_ataque_efectivo = max(0, otro_jugador.ataque - self.defensa)

        # si hay empate 
        if mi_ataque_efectivo == otro_ataque_efectivo:
            opciones_empate = [
                f"{self} ha metido un triple de último segundo en el tiempo extra, ¡ha ganado!\n",
                f"El jugador {otro_jugador} se lesionó en el tiempo extra, {self} ha ganado.\n",
                f"{self} ha ganado debido a un bloqueo contra el tablero.\n",
                f"{self} ha ganado con una clavada sobre {otro_jugador}.\n"
            ]
            mensaje_empate = random.choice(opciones_empate)
            print(f"¡{self} y {otro_jugador} empataron! {mensaje_empate}")
            return self
        # no empate
        elif mi_ataque_efectivo > otro_ataque_efectivo:
            return self
        else:
            return otro_jugador
        


#esta funcion esta fuera de la clase
def generar_nombres(base_nombres, adjetivos, cantidad):
    nombres_generados = set()
    while len(nombres_generados) < cantidad:
        base_nombre = random.choice(base_nombres)
        adjetivo = random.choice(adjetivos)
        nuevo_nombre = f"{base_nombre} el {adjetivo}"
        if nuevo_nombre not in nombres_generados:
            nombres_generados.add(nuevo_nombre)
    return list(nombres_generados)

# pedir la potencia para poder crear los objetos /// se que hasta 6 funciona con 2^7 mi pc no dio respuesta :,C 
potencia = int(input("Ingrese la potencia para determinar el número de peleadores(jugadores)(por ejemplo, para 2^3 ingrese 3): "))
cantidad_criaturas = 2 ** potencia

# basado en nombres de jugadores NBA / las listas se las pedi al chatGPT
base_nombres = ["Durantus", "LeBronix", "Currius", "Antetokus", "Hardinix", "Embiidor", "Leonardus", "Doncix"]
adjetivos = ["Rocoso", "Veloz", "Feroz", "Místico", "Poderoso", "Ágil", "Implacable", "Invisible"]

nombres = generar_nombres(base_nombres, adjetivos, cantidad_criaturas)

# generar n Jugadores
jugadores = [Criatura(nombre) for nombre in nombres]

print("-------------- Peleadores iniciales --------------")
contador = 1
for Individuo in jugadores:
    print(f"{contador}._ {Individuo}")
    contador += 1

rondas = 0
while len(jugadores) > 1:
    rondas += 1
    # aqui lo hice para que en la ultima ronda diga "Ronda Final" es más epico xD
    if len(jugadores) == 2:
        print(f"------- Ronda final -------")
    else:
        print(f"------- Ronda {rondas} -------")

    # que los enfrentamientos sean aleatorios (prueba)
    random.shuffle(jugadores)
    
    # nueva lista de ganadores para la siguiente ronda
    ganadores_ronda = []

    contador = 1
    for i in range(0, len(jugadores) - 1, 2):
        jugador1 = jugadores[i]
        jugador2 = jugadores[i+1]

        print(f"{contador}.-{jugador1} vs {jugador2}")
        contador += 1

        ganador_pelea = jugador1.pelear(jugador2)
        if ganador_pelea:
            ganadores_ronda.append(ganador_pelea)

    # actualizar la lista de jugadores con los ganadores de la ronda (se eliminan de la lista original los perdedores)
    jugadores = ganadores_ronda[:]

    if len(jugadores) != 1:
        # los grupos después de cada ronda
        print("\nJugadores restantes:")
        for jugador in jugadores:
            print(f"- {jugador}")

# el ultimo jugador en la lista es el ganador
print("------- ¡El campeón del Título! -------\n")
print(f"             {jugadores[0]}\n")
print(f"¡Se necesitaron {rondas} rondas para encontrar al ganador!")
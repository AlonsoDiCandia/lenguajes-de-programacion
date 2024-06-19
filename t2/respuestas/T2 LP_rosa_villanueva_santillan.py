#El codigo se realizo con algunas consultas a chatgpt y a llama (IA)y aprendizajes en clases .
#la idea era comprender y aprender los metodos ,funciones y como poder usarlos 
#TALLER DE PROGRAMACION- TAREA 2
#ROSA VILLANUEVA

import random
# clase Criatura tiene atributos como: nombre, vida, ataque y defensa. Los métodos de la clase incluyen:
class Criatura:
    def __init__(self, nombre, vida, ataque, defensa): # __init__(Constructor que inicializa los atributos de la criatura.)
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    def get_nombre(self):  # Métodos que use para  obtener los atributos
        return self.__nombre

    def get_vida(self):
        return self.__vida

    def get_ataque(self): #Este Métodos me permiten obtener los valores de los atributos.
        return self.__ataque

    def get_defensa(self):  
        return self.__defensa

    def set_vida(self, nueva_vida):  # Métodos que nos permiten modificar los valores de los atributos, pero solo a través algunos métodos.
        if nueva_vida >= 0:
            self.__vida = nueva_vida

    def set_ataque(self, nuevo_ataque):
        if nuevo_ataque >= 0:
            self.__ataque = nuevo_ataque

    def set_defensa(self, nueva_defensa):
        if nueva_defensa >= 0:
            self.__defensa = nueva_defensa

    def __str__(self):  # Sobrecargar el método __str__ para imprimir el nombre de la criatura
        return self.__nombre

    def mostrar_estado(self): # Método para imprimir el estado actual de la criatura
        return f'Nombre: {self.__nombre}, Vida: {self.__vida}, Ataque: {self.__ataque}, Defensa: {self.__defensa}'
    # Método  combatir contra otra criatura
    def combatir(self, otra):
        # Fórmula simple de combate: ataque - defensa del oponente
        dano_a_otra = self.__ataque - otra.get_defensa()
        dano_a_otra = max(dano_a_otra, 0) # El daño no puede ser negativo
        dano_a_esta = otra.get_ataque() - self.__defensa
        dano_a_esta = max(dano_a_esta, 0)

        self.set_vida(self.get_vida() - dano_a_esta)
        otra.set_vida(otra.get_vida() - dano_a_otra)

        if self.get_vida() > 0 and otra.get_vida() <= 0:
            print(f"{self.get_nombre()} gana el combate contra {otra.get_nombre()}")
            return self
        elif otra.get_vida() > 0 and self.get_vida() <= 0:
            print(f"{otra.get_nombre()} gana el combate contra {self.get_nombre()}")
            return otra
        elif self.get_vida() > 0 and otra.get_vida() > 0:
            ganador = random.choice([self, otra])
            print(f"El combate es , {ganador.get_nombre()} es elegido al azar como el ganador")
            return ganador
# Función que sirve para generar una lista de criaturas siguiendo la secuencia de potencias de 2
def generar_criaturas(n):
    nombres_base = ["Dragón", "Argos", "Centauro", "Gorgona", "Minotauro", "Medusa", "Odiseo", "Mantícora"]
    criaturas = []
    for i in range(n):
        nombre = f"{nombres_base[i % len(nombres_base)]} {i+1}"
        vida = random.randint(30, 100)
        ataque = random.randint(20, 60)
        defensa = random.randint(10, 50)
        criatura = Criatura(nombre, vida, ataque, defensa)
        criaturas.append(criatura)
    return criaturas
# Función para realizar el torneo de eliminación directa
def torneo_eliminacion_directa(criaturas):
    ronda = 1
    historico_rondas = []  # Lista para almacenar la historia de cada ronda


    while len(criaturas) > 1:
        print(f"\nRonda {ronda} del torneo:")
        ganadores = []
        ronda_actual = [] # Lista para almacenar los combates de la ronda actual
        for i in range(0, len(criaturas), 2):
            ganador = criaturas[i].combatir(criaturas[i + 1])
            ganadores.append(ganador)
            ronda_actual.append((criaturas[i], criaturas[i + 1], ganador))
            # Almacenar la ronda actual en el historial
        historico_rondas.append(ronda_actual)
         # Actualizar la lista de criaturas solo con los ganadores
        criaturas = ganadores
        ronda += 1
    # Anunciar el campeón del torneo
    print(f"\nEL CAMPEON DEL TORNEO ES  {criaturas[0].get_nombre()}")
    # Imprimir la historia del torneo
    print("\nHISTORIA DEL TORNEO:")
    for ronda_idx, ronda in enumerate(historico_rondas, 1):
        print(f"\nRonda {ronda_idx}:")
        for combate in ronda:
            criatura1, criatura2, ganador = combate
            print(f"{criatura1.get_nombre()} vs {criatura2.get_nombre()} -> Ganador: {ganador.get_nombre()}")

def torneo_todos_contra_todos(criaturas):
    puntajes = {criatura: 0 for criatura in criaturas}
    for i in range(len(criaturas)):
        for j in range(i + 1, len(criaturas)):
            ganador = criaturas[i].combatir(criaturas[j])
            if ganador == criaturas[i]:
                puntajes[criaturas[i]] += 3
            elif ganador == criaturas[j]:
                puntajes[criaturas[j]] += 3
            else:
                puntajes[criaturas[i]] += 1
                puntajes[criaturas[j]] += 1

    print("\nPuntajes finales:")
    for criatura, puntos in puntajes.items():
        print(f"{criatura.get_nombre()}: {puntos} puntos")

# Ejemplo de uso
criaturas = generar_criaturas(32)
print("Criaturas participantes:")
for criatura in criaturas:
    print(criatura.mostrar_estado())

torneo_eliminacion_directa(criaturas)
torneo_todos_contra_todos(criaturas)


import random
from time import sleep

class Criaturas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(50, 100)
        self.attack = random.randint(5, 10)
        self.defensa = random.randint(20, 30)
        self.rapidez = random.randint(1, 20)

    def modificar_vida(self, cantidad):
        self.vida += cantidad

    def modificar_attack(self, cantidad):
        self.attack += cantidad

    def modificar_defensa(self, cantidad):
        self.defensa += cantidad

    def modificar_rapidez(self, cantidad):
        self.rapidez += cantidad

    def recalcular_rapidez(self):
        self.rapidez = random.randint(1, 20)

    def reiniciar_defensa(self):
        self.defensa = random.randint(20, 30)

    def __str__(self):
        return self.nombre

Eliminados = []
Torneo = ["Bastian", "Vicente", "Andres", "Martin", "Cristian Lara", "Guaton Suppa", "Anorexico lucas", "Cubano"]
criaturas = []
random.shuffle(Torneo)


for nombre in Torneo:
    p = Criaturas(nombre)
    criaturas.append(p)

def FasesT(fase_nombre, fase_actual):
    print("#" * 20, fase_nombre, "#" * 20)
    for i, criatura in enumerate(fase_actual, 1):
        print(f"Peleador {i}: {criatura}")
    print("\n")
ganador = []
def realizar_pelea(fase_nombre, fase_actual):
    while len(fase_actual) > 1:
            FasesT(fase_nombre, fase_actual)
            siguiente_fase = []
            for i in range(0, len(fase_actual), 2):
                Criatura1 = fase_actual[i]
                Criatura2 = fase_actual[i + 1]

                print(f"Va a pelear {Criatura1} contra {Criatura2}\n")
                
                if fase_nombre == "Final":
                    if Criatura1.rapidez > Criatura2.rapidez:
                        print(f"--- {Criatura1} --- Tiene una rapidez mayor a la de --- {Criatura2} --- por lo que ataca antes")
                        sleep(1)
                        Criatura2.modificar_defensa(-Criatura1.attack)
                        if Criatura2.defensa <= 0:
                            print(f"La defensa de --- {Criatura2} --- es nula")
                            print(f"{Criatura2} ESTÁ FUERA DE COMBATE, GANA {Criatura1}\n")
                            Eliminados.append(Criatura2)
                            siguiente_fase.append(Criatura1)
                            ganador.append(Criatura1.nombre)
                            break

                        Criatura1.modificar_defensa(-Criatura2.attack)
                        if Criatura1.defensa <= 0:
                            print(f"La defensa de --- {Criatura1} --- es nula")
                            print(f"{Criatura1} ESTÁ FUERA DE COMBATE, GANA {Criatura2}\n")
                            Eliminados.append(Criatura1)
                            siguiente_fase.append(Criatura2)
                            ganador.append(Criatura2.nombre)
                            break

                    elif Criatura2.rapidez > Criatura1.rapidez:
                        print(f"--- {Criatura2} --- Tiene una rapidez mayor a la de --- {Criatura1} --- por lo que ataca antes")
                        sleep(1)
                        Criatura1.modificar_defensa(-Criatura2.attack)
                        if Criatura1.defensa <= 0:
                            print(f"La defensa de --- {Criatura1} --- es nula")
                            print(f"--- {Criatura1} --- ESTÁ FUERA DE COMBATE, GANA --- {Criatura2} ---\n")
                            Eliminados.append(Criatura1)
                            siguiente_fase.append(Criatura2)
                            ganador.append(Criatura2.nombre)
                            break

                        Criatura2.modificar_defensa(-Criatura1.attack)
                        if Criatura2.defensa <= 0:
                            print(f"La defensa de --- {Criatura2} --- es nula")
                            print(f"--- {Criatura2} --- ESTÁ FUERA DE COMBATE, GANA --- {Criatura1} ---\n")
                            Eliminados.append(Criatura2)
                            ganador.append(Criatura1.nombre)
                            break
                    else:
                        print(f"--- Empate en rapidez entre {Criatura1} y {Criatura2} --- Recalculando velocidades\n")
                        Criatura1.recalcular_rapidez()
                        Criatura2.recalcular_rapidez()
                        
                     
                while True:
                    if Criatura1.rapidez > Criatura2.rapidez:
                        print(f"--- {Criatura1} --- Tiene una rapidez mayor a la de --- {Criatura2} --- por lo que ataca antes")
                        sleep(1)
                        Criatura2.modificar_defensa(-Criatura1.attack)
                        if Criatura2.defensa <= 0:
                            print(f"La defensa de --- {Criatura2} --- es nula")
                            print(f"{Criatura2} ESTÁ FUERA DE COMBATE, GANA {Criatura1}\n")
                            Eliminados.append(Criatura2)
                            siguiente_fase.append(Criatura1)
                            break

                        Criatura1.modificar_defensa(-Criatura2.attack)
                        if Criatura1.defensa <= 0:
                            print(f"La defensa de --- {Criatura1} --- es nula")
                            print(f"{Criatura1} ESTÁ FUERA DE COMBATE, GANA {Criatura2}\n")
                            Eliminados.append(Criatura1)
                            siguiente_fase.append(Criatura2)
                            break

                    elif Criatura2.rapidez > Criatura1.rapidez:
                        print(f"--- {Criatura2} --- Tiene una rapidez mayor a la de --- {Criatura1} --- por lo que ataca antes")
                        sleep(1)
                        Criatura1.modificar_defensa(-Criatura2.attack)
                        if Criatura1.defensa <= 0:
                            print(f"La defensa de --- {Criatura1} --- es nula")
                            print(f"--- {Criatura1} --- ESTÁ FUERA DE COMBATE, GANA --- {Criatura2} ---\n")
                            Eliminados.append(Criatura1)
                            siguiente_fase.append(Criatura2)
                            break

                        Criatura2.modificar_defensa(-Criatura1.attack)
                        if Criatura2.defensa <= 0:
                            print(f"La defensa de --- {Criatura2} --- es nula")
                            print(f"--- {Criatura2} --- ESTÁ FUERA DE COMBATE, GANA --- {Criatura1} ---\n")
                            Eliminados.append(Criatura2)
                            siguiente_fase.append(Criatura1)
                            break
                    else:
                        print(f"--- Empate en rapidez entre {Criatura1} y {Criatura2} --- Recalculando velocidades\n")
                        Criatura1.recalcular_rapidez()
                        Criatura2.recalcular_rapidez()
            fase_actual = siguiente_fase[:]
            if fase_nombre == "Cuartos de final":
                fase_nombre = "Semi final"
            elif fase_nombre == "Semi final":
                fase_nombre = "Final"
realizar_pelea("Cuartos de final", criaturas)


print("ELIMINADOS DEL TORNEO DEL PODER")
for criatura in Eliminados:
    print(criatura.nombre, "\n")
    sleep(1)

print("#"*30,"GANADOR DEL TORNEO DEL PODER","#"*30)
print("#"*30,ganador,"#"*30)



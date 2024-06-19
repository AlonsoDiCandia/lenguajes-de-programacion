import random
from random import choice
from random import randint

class Pelea:
    def __init__(self, nombre, vida, ataque, prob_critico):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.prob_critico = prob_critico
    def modificar_vida(self, cantidad):
        self.vida += cantidad
    def modificar_ataque(self, cantidad):
        self.ataque += cantidad
    def modificar_prob_critico(self, cantidad):
        self.prob_critico += cantidad
    def __str__(self):
        return self.nombre
# razas eliminadas = , "SRAM", "ANUTROF", "ZOBAL", "STEAMER", "SELOTROPE", "HIPERMAGO", "UGINAK", "FORJALANZAS"
nombres = ["SACRÓLITO", "SADIDA", "PANDAWA", "TYMADOR", "FECA", "XELOR", "OCRA", "OSAMODA", "YOPUKA", "ZURCARÁK", "ANIRIPSA"]
criaturas = []

# ESTE CICLO ES LARGO PQ QUISE DARLE CARACTERISTICAS UNICAS A CADA UNO DE LOS LUCHADORES (SON RAZAS DEL DOFUS)

#     nombre = random.choice(nombres) ----> aqui se escoge uno de los nombres que estan en la lista mediante se inicia el ciclo
#     if nombre == "SACRÓLITO": ----------> cada nombre conlleva hacia caracteristicas diferentes 
#         vida = random.randint(120, 140) > todas las caracteristicas van variando algunos seran mas resistentes pero tendran menos daño
#         ataque = random.randint(5, 10) -> es un tipo de sistema de equilibrio para que todos ganen a su manera
#         prob_critico = 0
#         criaturas.append(Pelea(nombre, vida, ataque, prob_critico))

for jugadores in range(8):
    nombre = random.choice(nombres)
    if nombre == "SACRÓLITO":
        vida = random.randint(120, 140)
        ataque = random.randint(5, 10)
        prob_critico = 0
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "SADIDA":
        vida = random.randint(80, 90)
        ataque = random.randint(20, 25)
        prob_critico = 20
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "PANDAWA":
        vida = random.randint(95, 100)
        ataque = random.randint(15, 20)
        prob_critico = 0
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "TYMADOR":
        vida = random.randint(80, 85)
        ataque = random.randint(10, 25)
        prob_critico = 50
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "FECA":
        vida = random.randint(110, 120)
        ataque = random.randint(10, 15)
        prob_critico = 10
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "XELOR":
        vida = random.randint(80, 90)
        ataque = random.randint(20, 25)
        prob_critico = 20
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "OCRA":
        vida = random.randint(60, 65)
        ataque = random.randint(25, 30)
        prob_critico = 40
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "OSAMODA":
        vida = random.randint(75, 80)
        ataque = random.randint(15, 25)
        prob_critico = 25
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "YOPUKA":
        vida = random.randint(80, 90)
        ataque = random.randint(10, 25)
        prob_critico = 20
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    elif nombre == "ZURCARÁK":
        vida = random.randint(75, 80)
        ataque = random.randint(15, 20)
        prob_critico = 35
        criaturas.append(Pelea(nombre, vida, ataque, prob_critico))
    

def combate(criatura1, criatura2):
    print(f"{criatura1}  /VS/ {criatura2} ")
    turno = 0
    while criatura1.vida > 0 and criatura2.vida > 0: #----> en el ciclo de la funcion combate se inicia la batalla la cual algunos dependeran de sus caracteristicas
        turno +=1
        # print(f"Turno {turno}")
        if random.randint(0,100) <= criatura1.prob_critico: # ----> se mide una probabilidad en un rango de 0 a 100 y si cae en la prob del PJ podra hacer un ataque critico
            dano = criatura1.ataque *2
            # print(f"{criatura1.nombre} realiza un ataque CRITICO!")
        else:
            dano = criatura1.ataque # ----> si la criatura no tuvo suerte solo hara el daño normal asignado :C
        # print(f"{criatura1.nombre} ha hecho un daño de {dano} hacia {criatura2.nombre}")
        criatura2.vida -= dano # ---> el daño despues de haber pasado en este proceso se lo restamos a la vida de la criatura contrincante 
        # print(f"la vida restante de {criatura2.nombre} es de {criatura2.vida}")

        if criatura2.vida <= 0: # -----> se verifica si la criatura contrincante sigue con vida 
            # print(f"{criatura2.nombre} ha sido derrotado!") # ---> si en este caso la criatura contrincante muere se retornara como ganadora la criatura1
            # print("-------------------------------------------------------------------------------------------------------")
            return criatura1
        # pero si sigue con vida se continuara la batalla
        
        if random.randint(0, 100) <= criatura2.prob_critico:
            dano2 = criatura2.ataque *2
            # print(f"{criatura2.nombre} realiza un ataque CRITICO!")
        else:
            dano2 = criatura2.ataque
        # print(f"{criatura2.nombre} ha hecho un daño de {dano2} hacia {criatura1.nombre}")
        criatura1.vida -= dano2
        # print(f"la vida restante de {criatura1.nombre} es de {criatura1.vida}")

        if criatura1.vida <= 0:
            # print(f"{criatura1.nombre} ha sido derrotado!")
            # print("-------------------------------------------------------------------------------------------------------")
            return criatura2
    print("-------------------------------------------------------------------------------------------------------")

def torneo(criaturas):
    if not criaturas:
        print("No hay criaturas para el torneo.")
        return None
    
    while len(criaturas) > 1:
        print("Nueva Ronda")
        print("-------------------------------------------------------------------------------------------------------")
        ganadores = []
        for i in range(0, len(criaturas) - 1, 2):
            ganador = combate(criaturas[i], criaturas[i + 1])
            ganadores.append(ganador)
            print(f"ganador de este combate es {ganador}")
            print("-------------------------------------------------------------------------------------------------------")
        # if len(criaturas) % 2 == 1:  
        #     ganadores.append(criaturas[-1])
        criaturas = ganadores
    return criaturas[0]
print(criaturas)
ganador = torneo(criaturas)

if ganador:
    print(f"\n!!!!La criatura ganadora es: {ganador}!!!!!")
    print("*Proceden a explotar fuegos artificiales")
    lista_de_los_doce = ["Dokoko", "Dofus Esmeralda", "Dofus Ocre", "Dofus Purpura", "Dofus Kalipto", "Dofus Vulbis", "Dofus Ébano", "Dofus de los Hielos", "Dofus Zanahowia", "Dofawa :(", "Dofus Turquesa", "Dolmanax"]
    print(f"Ahora {ganador} obtuvo como premio {random.choice(lista_de_los_doce)} que es uno de los doce!!")
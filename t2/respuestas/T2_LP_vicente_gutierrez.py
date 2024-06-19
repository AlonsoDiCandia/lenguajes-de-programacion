import random       #la ocuparé para hacer sorteos y para los atributos de la clase

class criatura():
    def __init__(self, nombre):
        self.nombre = nombre
        ataque = random.randint(10,40)
        self.ataque = ataque 
        defensa = random.randint(10,40)
        self.defensa = defensa   
        self.vida = 100        #Establecí la vida en 100 para todos              

    def atacar(self,enemigo):   #Hice que la defensa resista un porcentaje del ataque
        aguanta = enemigo.defensa/100
        enemigo.vida = enemigo.vida-(self.ataque-(aguanta*self.ataque))

    def restaurar_vida(self):   #Hice que se restaure su vida tras cada combate
        self.vida = 100         #para hacerlo más justo

    def nombre_criatura(self):  #Para que pueda saludar con su nombre
        saludo_1 = "Hola, me presento soy "
        saludo_2 = "Buenas, me llamo "
        saludos = [saludo_1,saludo_2]
        saludo = random.choice(saludos)
        print(f"{saludo}{self.nombre}")

participantes = []
numero_llaves = int(input("Ingrese el numero de llaves del torneo: "))
while numero_llaves < 3:
    numero_llaves = int(input("Ingrese un numero válido (mínimo 3 llaves): "))

for creacion in range(2**numero_llaves):    #Creando los participantes
    nombre = input(f"Nombre para la {creacion+1}° criatura : ")
    nueva_criatura = criatura(nombre)
    nueva_criatura.nombre_criatura()
    participantes.append(nueva_criatura)

random.shuffle(participantes)        #Haciendo random el orden para el sorteo

contador_peleas = 1
for rondas in range(numero_llaves):
    print(f"{"="*15} Bracket {"="*15}")
    for peleas in range(0, len(participantes), 2): #Para darle formato al bracket
        peleador_1 = participantes[peleas]
        peleador_2 = participantes[peleas+1]
        if contador_peleas % 2 != 0 and peleas != len(participantes)-2:
            print(f"{peleador_1.nombre} v/s {peleador_2.nombre}")
            print(f"{"="*7}{">"*5} Ganadores por definir {"="*4}")
        else:
            print(f"{peleador_1.nombre} v/s {peleador_2.nombre}")
            print("="*40)
        contador_peleas+=1

    restantes = []
    if rondas == numero_llaves-1:   #Para ver como van las peleas del bracket
        print(f"{"="*10} Pelea ronda final {"="*10}")
    else:
        print(f"{"="*10} Peleas ronda {rondas+1} {"="*10}")

    for pelea in range(0, len(participantes), 2):   #Aqui enfrento a los peleadores
        participante_1 = participantes[pelea]
        participante_2 = participantes[pelea+1]
        print(f"Pelea {participante_1.nombre} contra {participante_2.nombre}")

        while participante_1.vida > 0 or participante_2.vida > 0:   #aqui se agarran a cachos
            quien_ataca = random.randint(0,1)
            if quien_ataca == 0:
                participante_1.atacar(participante_2)
            else:
                participante_2.atacar(participante_1)
        if participante_2.vida > 0:             #Aqui se ve quien paso y restauro su vida
            print(f"{participante_2.nombre} venció a {participante_1.nombre}")
            print(f"{participante_2.nombre} pasa de fase")
            participante_2.restaurar_vida()
            restantes.append(participante_2)
        else:   
            print(f"{participante_1.nombre} venció a {participante_2.nombre}")
            print(f"{participante_1.nombre} pasa de fase")
            participante_1.restaurar_vida()
            restantes.append(participante_1)
        print(f"{"="*40}")
    participantes = restantes

print(f"El gran campeón de criaturas de noche de viernes es ¡{restantes[0].nombre}!, ¡felicitaciones!")

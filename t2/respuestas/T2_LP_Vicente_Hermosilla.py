################################ Tarea 2 ###################################
################### Vicente Hermosilla Paralelo 701 ########################
import random

class pinguino:
    def __init__(self, nombre):
        tipos_Elemento = ['Agua', 'Fuego', 'Tierra', 'Aire'] #Agua le gana a Fuego--Fuego le gana a Tierra--Tierra le gana a Aire--Aire le Gana a Agua--
        self.nombre = nombre
        self.vida = random.randint(20,50)
        self.ataque = random.randint(5,30)
        self.defensa = random.randint(1,20)
        self.tipo = random.choice(tipos_Elemento)
        self.puntos = 0
    
        
    def __str__(self):
        return self.nombre

    def comparacion_elemento(self, oponente):
        ventajas = {
            'Agua': 'Fuego',
            'Fuego': 'Tierra',
            'Tierra': 'Aire',
            'Aire': 'Agua'
        }
        if ventajas[self.tipo] == oponente.tipo:
            print(f'\n --El {self.nombre} tiene ventaja sobre su oponente debido a que el es de tipo {self.tipo} y pelea contra el {oponente.nombre} el cual es tipo {oponente.tipo}--')
            return 2, 0.5
        elif ventajas[oponente.tipo] == self.tipo:
            print(f'\n --El {oponente.nombre} tiene ventaja sobre su oponente debido a que el es de tipo {oponente.tipo} y pelea contra el {self.nombre} el cual es tipo {self.tipo}--')
            return 0.5, 2
        else:
            print(f'\n --Ambos tienen el mismo tipo de elemento por ende no hay ventaja de uno sobre otro--')
            return 1, 1
     
    
    def pelea(self, contrincante):
        
        ventaja_self, ventaja_contrincante  = self.comparacion_elemento(contrincante)
        while self.vida > 0 and contrincante.vida > 0:

            #Variables que muestran el daño recibido por cada pinguino donde se le resta la defensa para disminuir el ataque
            danio_recibido_self = round(max(contrincante.ataque * ventaja_contrincante  - self.defensa, 1), 0)
            danio_recibido_contrincante = round(max(self.ataque * ventaja_self - contrincante.defensa, 1), 0)

            #Se le resta el daño recibido a la vida de cada pinguino
            contrincante.vida -= round(danio_recibido_contrincante, 0)
            self.vida -= round(danio_recibido_self, 0)

            print(f'\n{self.nombre} ataca a {contrincante.nombre}!! causando {danio_recibido_contrincante} de daño. Vida restante de {contrincante.nombre}: {contrincante.vida}')
            print(f'{contrincante.nombre} ataca a {self.nombre}!! causando {danio_recibido_self} de daño. Vida restante de {self.nombre}: {self.vida}')

            #Se verifica si algun pinguino tiene vida menor o igual a 0
            if self.vida <= 0:
                print(f'\n--- {self.nombre} ha sido derrotado por {contrincante.nombre}!! :O ---')
                return contrincante
            elif contrincante.vida <= 0:
                print(f'\n--- {contrincante.nombre} ha sido derrotado por {self.nombre}!! :O ---')
                return self
            
    def curar(self):
        curacion = random.randint(15,25)
        self.vida += curacion
        print(f'-- {self.nombre} fue curado con {curacion} puntos de salud, tiene ahora una cantidad de vida de {self.vida} :D --')

#Función donde ocurre el torneo y se van eliminando pinguinos y retornamos al ganador y un diccionario con los registros de las peleas
def torneo(lista_luchadores):

    peleas = {}
    num_ronda = 1
    num_fase = 1
    while len(lista_luchadores) > 1:
        print(f'\n==================== Fase {num_fase} ====================\n')
        peleas_ronda = []
        ganadores = []
        while len(lista_luchadores) > 1:
            pinguino1 = random.choice(lista_luchadores)
            pinguino2 = random.choice(lista_luchadores)
            
            while pinguino1 == pinguino2:
                pinguino2 = random.choice(lista_luchadores)
                
            print(f'\n================= Ronda {num_ronda} ================\n')

            print(f'\n~~~~~~~~~~~~~~~~ Se va a enfrentar el {pinguino1.nombre} contra el {pinguino2.nombre}!!!!!!!!!!!!!! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')  
            ganador = pinguino1.pelea(pinguino2)
            print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~ El ganador de esta ronda es el {ganador}!!!!! PASA A LA SIGUIENTE FASE!!! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
           
            #Se cura la vida del ganador para que no pierda tan rapido en su siguiente pelea
            print(f'\n-- El {ganador} va a curar sus heridas a la enfermeria para su proximo combate en la siguente fase ;) --')
            ganador.curar()

            #Se remueve de la lista el pinguino que perdio la ronda
            if pinguino1 != ganador:
                lista_luchadores.remove(pinguino1)
            elif pinguino2 != ganador:
                lista_luchadores.remove(pinguino2)

            #El ganador de la pelea va a otra lista para que no pelee en la misma ronda y pase a la siguiente fase
            ganadores.append(ganador)
            lista_luchadores.remove(ganador)

            #Guardar en un diccionario registro de las peleas
            peleas_ronda.append(f"Ronda {num_ronda}: {pinguino1} vs {pinguino2} ----> Ganador: {ganador}")
            num_ronda += 1

        if len(pinguinos_inscritos) == 1:
            ganadores.append(lista_luchadores.pop(0))

        lista_luchadores = ganadores
        peleas[f'Fase {num_fase}'] = peleas_ronda
        num_fase += 1

    return lista_luchadores[0], peleas


#Funcion donde todos pelean contra todos y el ganador se elige mediante puntos
def todos_contra_todos(lista_peleadores):
    resultados = {}
    pelea_numero = 1
    i = 0

    while i < len(lista_peleadores):
        j = i + 1

        while j < len(lista_peleadores):

            pinguino1 = lista_peleadores[i]
            pinguino2 = lista_peleadores[j]

            print(f'\n------------Pelea {pelea_numero}: {pinguino1.nombre} vs {pinguino2.nombre}!!!!!--------------------------')  
            ganador = pinguino1.pelea(pinguino2)

            #Al ganador se le otorgan 3 puntos y en caso de empate 1 punto cada uno
            if ganador == pinguino1:
                pinguino1.puntos += 3

                print(f'\n--Gana el {pinguino1}, consigue 3 puntos !!!!!!!!!--')
                resultados[f'{pinguino1.nombre} vs {pinguino2.nombre}'] = f'Ganador: {pinguino1.nombre}'

            elif ganador == pinguino2:
                pinguino2.puntos += 3

                print(f'\n--Gana el {pinguino2}, consigue 3 puntos !!!!!!!!!--')
                resultados[f'{pinguino1.nombre} vs {pinguino2.nombre}'] = f'Ganador: {pinguino2.nombre}'

            else:
                pinguino1.puntos += 1
                pinguino2.puntos += 1

                print(f'\n--Ocurrio un empate, ambos ganan 1 punto!!!!!!!!!--')
                resultados[f'{pinguino1.nombre} vs {pinguino2.nombre}'] = 'Empate'

            #Se curan ambos pinguinos para que en la siguiente ronda no tengan tan poca vida
            pinguino1.curar()
            pinguino2.curar()
            print(f'\n-------- Ambos Pinguinos fueron curados :D --------')

            pelea_numero += 1
            j += 1
        i += 1
    
    #Usamos al primer pinguino como inicio para buscar quien tiene la mayor cantidad 
    ganador = lista_peleadores[0]
    #Recorremos las lista comparando los puntos y si los puntos del p actual es mayo al del ganador actual este se actualiza hasat llegar al que tiene mas puntos :)
    for p in lista_peleadores:
        if p.puntos > ganador.puntos:
            ganador = p
    
    return ganador, resultados

nombres = [

    "Pinguino Pirata",
    "Pingüino Minero",
    "Pinguino Danzarín",
    "Pingüino Borracho",
    "Pinguino Saltarín",
    "Pingüino Ninja",
    "Pinguino Aventurero",
    "Pingüino Risueño"
]
pinguinos_inscritos = []

print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EMPEZO EL 1ER TORNEO DE CLUB PENGUIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SE INSCRIBIERON 8 PINGUINOS LOS CUALES SON:  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
#Los nombres de los pinguines se convierten en objetos los cuales se meten a una lista
while len(nombres) != 0:
    nombre = random.choice(nombres)
    pinguino_nuevo = pinguino(nombre)
    pinguinos_inscritos.append(pinguino_nuevo)
    nombres.remove(nombre)

for n in pinguinos_inscritos:
    print(f'{n} el cual tiene un ataque de {n.ataque}, una defensa de {n.defensa} y un nivel de vida de {n.vida} y domina el tipo {n.tipo}')

#Se elige el tipo de torneo a realizar
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Tipos de torneo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Para un torneo con eliminaciones en estilo llave elija 1 \n Para un torneo todos contra todos elija 0 ')
tipo_torneo = int(input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Elija que tipo de torneo que quiere: '))

if tipo_torneo == 1:
    print('\n------------------------------------------------------- Se eligio el tipo de torneo con eliminaciones tipo llave!!! ------------------------------------------------------------- ')
    #Se llama a la funcion del torneo la cual recibe la lista de los pinguinos y esta retorna al ganador y una lista con un registro del torneo
    ganador, registro_peleas = torneo(pinguinos_inscritos)

    print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EL CAMPEÓN DEL 1ER TORNEO DE CLUB PENGUIN ES EL {ganador} !!!!!!!!!! :DDD ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    #Imprimir cada ronda sus respectivos luchadores
    print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ De esta manera se dieron las peleas hasta la fase final del torneo: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for fase, peleas_ronda in registro_peleas.items():
        print(f'\n-- {fase} --')
        for pelea in peleas_ronda:
            print(f'  {pelea}')

elif tipo_torneo == 0:
    print('\n------------------------------------------------------- Se eligio el tipo de torneo de todos contra todos!!! ------------------------------------------------------------- ')
    campeon, registro_peleas = todos_contra_todos(pinguinos_inscritos)
    print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EL CAMPEÓN DEL 1ER TORNEO TODOS CONTRA TODOS DE CLUB PENGUIN ES EL {campeon} !!!!!!!!!! :DDD ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Puntos del campeón: {campeon.puntos} !!!!!!! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    #Imprimimos todas las peleas que ocurrieron y sus ganadores
    print(f'\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ De esta manera se dieron las peleas en el torneo todos contra todos: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for pelea, resultado in registro_peleas.items():
        print(f'--{pelea}--: \n --{resultado} :)--\n')


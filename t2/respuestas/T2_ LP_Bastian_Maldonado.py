import random
from random import choice
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"
NEGRO = "\033[30m"
RESET = "\033[0m"
class Cantantes:
    def __init__(self, nombre):
        self.nombre = nombre
        self.live = 40
    def __str__(self):
        return self.nombre

    def combos(self):
        palabrazo = {
            "TIRADERA": 10,
            "DOBLE TEMPO": 15,
            "COLABORACION CON FUTURE": 20,
            "BIZARAP SESION": 10,
        }
        elegir_ataque = choice(list(palabrazo.keys()))
        eleccion = palabrazo[elegir_ataque]

        print(f'{self.nombre} va a usar {elegir_ataque}')
        return eleccion

    def peleas(self, peleador):
        print(f"PELEA: {self.nombre} v/s {peleador.nombre}")
        contador = 1
        while self.live > 0 and peleador.live > 0:
            print(f"ATAQUE {contador}")
            ataque1 = self.combos()
            ataque2 = peleador.combos()
            peleador.live -= ataque1
            self.live -= ataque2
            
            if self.live <= 0:
                print(f'{self.nombre} ha sido derrotado por {peleador.nombre}')
                # return peleador
            if peleador.live <= 0:
                print(f'{peleador.nombre} ha sido derrotado por {self.nombre}')
                # return self
            if peleador.live <= 0 and self.live <= 0:
                print('mueren ambos'*20)
            contador += 1
        contador = 1
        return 

nombres_cantantes = [
    f"{ROJO}Kanye West{RESET}",
    f"{MAGENTA}Kendrick Lamar{RESET}",
    f"{VERDE}Drake{RESET}",
    f"{AZUL}XXXTENTACION{RESET}",
    f"{AMARILLO}Tyler, The Creator{RESET}",
    f"{CYAN}Travis Scott{RESET}",
    f"{NEGRO}Lil pump{RESET}",
    f"{BLANCO}Lil Tecca{RESET}"
]

cantantes_lista = [Cantantes(nombre) for nombre in nombres_cantantes]

cantante1 = choice(cantantes_lista); cantantes_lista.remove(cantante1)
cantante2 = choice(cantantes_lista); cantantes_lista.remove(cantante2)
cantante3 = choice(cantantes_lista); cantantes_lista.remove(cantante3)
cantante4 = choice(cantantes_lista); cantantes_lista.remove(cantante4)
cantante5 = choice(cantantes_lista); cantantes_lista.remove(cantante5)
cantante6 = choice(cantantes_lista); cantantes_lista.remove(cantante6)
cantante7 = choice(cantantes_lista); cantantes_lista.remove(cantante7)
cantante8 = choice(cantantes_lista); cantantes_lista.remove(cantante8)

## BIENVENIDA
bienvenida = f'''{AZUL}#########################################################################################################################################################################################################
_____________________________________________#BIENVENIDOS A LA BATALLA DE RAPEROS MÁS GRANDE DE LA HISTORIA#_____________________________________________________________________________________________
#########################################################################################################################################################################################################{RESET}
_________________LOS PARTICIPANTES SON:__________________________________________________________________________________________________________________________________________________________________
_______________________________________{cantante1.nombre}, {cantante2.nombre}, {cantante3.nombre}, {cantante4.nombre}, {cantante5.nombre}, {cantante6.nombre}, {cantante7.nombre}, {cantante8.nombre}____________________________________________________________
{AZUL}#########################################################################################################################################################################################################{RESET}
'''; print(bienvenida)
print("    ")
print(F"{AMARILLO}____________________________________________________________________________#PRIMER RONDA#____________________________________________________________________________________________________{RESET}")
print(F"{AMARILLO}#########################################################################################################################################################################################################{RESET}")
ganador_primer_round1 = cantante1.peleas(cantante2)
ganador_primer_round1.live = 20  
print(F"{AMARILLO}#########################################################################################################################################################################################################{RESET}")
ganador_primer_round2 = cantante3.peleas(cantante4)
ganador_primer_round2.live = 20  
print(F"{AMARILLO}#########################################################################################################################################################################################################{RESET}")
ganador_primer_round3 = cantante5.peleas(cantante6)
ganador_primer_round3.live = 20  
print(F"{AMARILLO}#########################################################################################################################################################################################################{RESET}")
ganador_primer_round4 = cantante7.peleas(cantante8)
ganador_primer_round4.live = 20  
print(F"{AMARILLO}#########################################################################################################################################################################################################{RESET}")
print("    ")
print(F"{AZUL}____________________________________________________________________________#SEGUNDO RONDA#___________________________________________________________________________________________________{RESET}")
print(F"{AZUL}#########################################################################################################################################################################################################{RESET}")

ganador_segunda_round1 = ganador_primer_round1.peleas(ganador_primer_round2)
ganador_segunda_round1.live = 20  
print(F"{AZUL}#########################################################################################################################################################################################################{RESET}")
ganador_segunda_round2 = ganador_primer_round3.peleas(ganador_primer_round4)
ganador_segunda_round2.live = 20  
print(F"{AZUL}#########################################################################################################################################################################################################{RESET}")
print("    ")
print(F"{VERDE}____________________________________________________________________________#RONDA FINAL#___________________________________________________________________________________________________{RESET}")
print(F"{VERDE}#########################################################################################################################################################################################################{RESET}")

gran_final = ganador_segunda_round1.peleas(ganador_segunda_round2)
gran_final.live = 20  
print(F"{VERDE}#########################################################################################################################################################################################################{RESET}")
print(f"EL GANADOR DEFINITIVO ES {gran_final.nombre}")
print(F"{VERDE}#########################################################################################################################################################################################################{RESET}")




     

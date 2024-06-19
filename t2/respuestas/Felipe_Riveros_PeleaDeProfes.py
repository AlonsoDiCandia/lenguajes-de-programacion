import random
from random import choice
import tkinter as tk

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.attack = random.randint(1, 10)
        self.deff = random.randint(1, 5)
        self.tipo_ataque = random.choice(["Calculo", "Informática", "Cancer","Arq. Computadores", "Adm. Empresas", "Fisica", "Base De Datos", "Lengua de programacion", "DEI","Pan con Mayo"])
        self.c_dicta = random.choice(["Calculo", "Informática", "Cancer","Arq. Computadores", "Adm. Empresas", "Fisica", "Base De Datos", "Lengua de programacion", "DEI","Pan con Mayo"])

    def __str__(self):
        return self.nombre

nombres_para_profesores = [
    "Jose Carrasco",
    "J Briones",
    "Emilio",
    "J arellano",
    "Diaz",
    "Overfloooooow",
    "Catalan",
    "Alvaro galaz",
    "Juan gonzales",
    "Eduardo Urrutia",
    "Agus Diaz",
    "Martin",
    "Angus",
]
ciudades_para_profesores = ["Talca",
"Valpo",
"Hualpen",
"Hualqui",
"Chiloe",
"Tumbe",
"Huachipato",
"Chillan",
"Conce",
"La Udec"]

profesores = []
n = int(input("Ingrese la cantidad de profesores (debe ser un número par): "))
while n % 2 != 0:
    print("El número debe ser par. Intente nuevamente.")
    n = int(input("Ingrese la cantidad de profesores (debe ser un número par): "))

nombres_usados = []
for _ in range(n):
    if nombres_para_profesores:
        # Si todavía hay nombres de profesores disponibles, úsalos
        nombre = choice(nombres_para_profesores)
        nombres_para_profesores.remove(nombre)
        nombres_usados.append(nombre)
    else:
        # Si no hay nombres de profesores disponibles, genera uno con el formato "nombre del profesor de lugar"
        nombre_profesor = choice(nombres_usados)
        ciudad = choice(ciudades_para_profesores)
        ciudades_para_profesores.remove(ciudad)
        nombre = f"{nombre_profesor} de {ciudad}"
    p = Profesor(nombre)
    profesores.append(p)
peleadores = {}

for i, profesor in enumerate(profesores[:n]):
    peleadores[f'Peleador {i+1}'] = profesor

def sistema_todos_contra_todos(peleadores):
    peleadores = list(peleadores.values())  # Convierte el diccionario en una lista
    resultados = {peleador: 0 for peleador in peleadores}  # Inicializa los resultados

    for i in range(len(peleadores)):
        for j in range(i+1, len(peleadores)):
            peleador1 = peleadores[i]
            peleador2 = peleadores[j]
            print(f'Va a pelear {peleador1.nombre} vs {peleador2.nombre}')
            
            # Aumenta el daño del profesor si ataca en su campo de especialización
            if peleador1.tipo_ataque == peleador1.c_dicta:
                peleador1.attack *= 1.3
                print(f"{peleador1.nombre} se benefició del bono de ataque por la especialidad : {peleador1.tipo_ataque}")
                
            if peleador2.tipo_ataque == peleador2.c_dicta:
                peleador2.attack *= 1.3
                print(f"{peleador2.nombre} se benefició del bono de ataque por la especialidad : {peleador2.tipo_ataque}")
            if peleador1.attack > peleador2.attack:
                resultados[peleador1] += 3
                print(f'{peleador1.nombre} ganó la pelea contra {peleador2.nombre}')
            elif peleador2.attack > peleador1.attack:
                resultados[peleador2] += 3
                print(f'{peleador2.nombre} ganó la pelea contra {peleador1.nombre}')
            else:
                # En caso de empate, ambos peleadores reciben 1 punto
                print(f'Hubo un empate entre {peleador1.nombre} y {peleador2.nombre}')
                resultados[peleador1] += 1
                resultados[peleador2] += 1

    # Ordena los peleadores por la cantidad de puntos
    peleadores = sorted(resultados, key=resultados.get, reverse=True)

    return peleadores

def sistema_eliminatorio(peleadores):
    peleadores = list(peleadores.values())  # Convierte el diccionario en una lista
    perdedores = []  # Lista para guardar a los perdedores de cada ronda
    while len(peleadores) > 1:
        nuevos_ganadores = []
        nuevos_perdedores = []
        random.shuffle(peleadores)  # Mezcla la lista de peleadores
        for i in range(0, len(peleadores), 2):
            peleador1 = peleadores[i]
            if i+1 < len(peleadores):  # Asegúrate de que i+1 es un índice válido
                peleador2 = peleadores[i+1]
                print(f'Va a pelear {peleador1.nombre} vs {peleador2.nombre}')
                ataque_original_peleador1 = peleador1.attack
                ataque_original_peleador2 = peleador2.attack
                if peleador1.c_dicta == peleador1.tipo_ataque:
                    peleador1.attack *= 1.2
                    print(f"{peleador1.nombre} se benefició del bono de ataque por la especialidad : {peleador1.tipo_ataque}")
                if peleador2.c_dicta == peleador2.tipo_ataque:
                    peleador2.attack *= 1.2
                    print(f"{peleador2.nombre} se benefició del bono de ataque por la especialidad : {peleador2.tipo_ataque}")
                if peleador1.attack > peleador2.attack:
                    nuevos_ganadores.append(peleador1)
                    nuevos_perdedores.append(peleador2)
                    print(f'El ganador es {peleador1.nombre}')
                elif peleador2.attack > peleador1.attack:
                    nuevos_ganadores.append(peleador2)
                    nuevos_perdedores.append(peleador1)
                    print(f'El ganador es {peleador2.nombre}')
                else:
                    # En caso de empate, elige un ganador al azar
                    ganador = random.choice([peleador1, peleador2])
                    perdedor = peleador1 if ganador == peleador2 else peleador2
                    print(f'Hubo un empate, pero {ganador.nombre} ganó en el sorteo')
                    nuevos_ganadores.append(ganador)
                    nuevos_perdedores.append(perdedor)
                peleador1.attack = ataque_original_peleador1
                peleador2.attack = ataque_original_peleador2
            else:
                # Si hay un número impar de peleadores, el último pasa a la siguiente ronda automáticamente
                nuevos_ganadores.append(peleador1)
        peleadores = nuevos_ganadores
        perdedores.extend(nuevos_perdedores)
    return peleadores[0]

#esta funcion se la pedi a una IA pq me dio latita hacerla y no tengo mucho tiempo pq tengo que viajar D:
#anyways, esta funcion es para mostrar los resultados en una ventana de tkinter

def mostrar_resultados():
    ventana = tk.Tk()
    ventana.title("Resultados de la pelea de profesores")
    
    # Sistema todos contra todos
    primeras_posiciones = sistema_todos_contra_todos(peleadores)
    resultados_todos_contra_todos = "Sistema todos contra todos:\n"
    for i, peleador in enumerate(primeras_posiciones.items(), start=1):
        key, value = peleador
        resultados_todos_contra_todos += f"Posición {i}: {key} {value}\n"
    
    # Sistema eliminatorio
    ganador = sistema_eliminatorio(peleadores)
    resultado_eliminatorio = f"El ganador del torneo es! {ganador.nombre}"
    
    # Crear etiquetas para mostrar los resultados
    label_todos_contra_todos = tk.Label(ventana, text=resultados_todos_contra_todos)
    label_eliminatorio = tk.Label(ventana, text=resultado_eliminatorio)
    
    # Mostrar las etiquetas en la ventana
    label_todos_contra_todos.pack()
    label_eliminatorio.pack()
    
    ventana.mainloop()

mostrar_resultados()


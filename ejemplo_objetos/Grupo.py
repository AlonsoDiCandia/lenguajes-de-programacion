import itertools

class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []
        self.partidos = []
        
    def __repr__(self):
        return self.nombre
    
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def generar_partidos(self):
        ida = list(itertools.combinations(self.equipos, 2))
        vuelta = list(map(lambda x: (x[1],x[0]), ida))
        partidos = ida + vuelta
        for partido in partidos:
            print(f'Combate entre: {partido[0]} y {partido[1]}')
        self.partidos = partidos











        
        

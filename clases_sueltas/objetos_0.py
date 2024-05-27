
class Perro:


    def __init__(self, nombre, raza, color):
        self.patas = 4
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.hambre = 10 # con -50 muere
        self.vivo = True
    
    def ladrar(self):
        print('Guau guau')
    
    def accidente(self, perdida):
        self.patas = self.patas - perdida

    def alimentar(self):
        comidas = {
            "Pollo cocido": 10,
            "Zanahorias": 10,
            "Arroz": 10,
            "Manzanas": 10,
            "Calabaza": 10,
            "Queso": 5,
            "Huevos cocidos": 5,
            "Pavo cocido": 5,
            "Avena": 5,
            "Papas cocidas": 5,
            "Chocolate": -100,
            "Cebolla y ajo": -20,
            "Uvas y pasas": -10,
            "Cacao": -100,
            "Huesos cocidos": -15
        }
        # for e,alimento in enumerate(comidas.keys()):
        #     print(f'{e}.- {alimento}')
        
        elegir_comida = input(f"Elija el alimento a dar a {self.nombre}: ")

        self.hambre += comidas[elegir_comida]

        print(f'{self.nombre} tiene {self.hambre} puntos de hambre')

        if self.hambre <= -50:
            self.vivo = False
        
        if not self.vivo:
            print(f'Lamentablemente {self.nombre} murio de hambre :c (lloremos T.T)')
        


# perro1 = Perro('Manjar', 'Meztiza', 'Cafe')
# perro2 = Perro('Galleta', 'Beagle', 'Blanco con cafe')

# print(f'{perro1.nombre} es de color {perro1.color}')
# print(f'{perro2.nombre} es de color {perro2.color}')

perro_nuevo = Perro('Carbonada', 'pug', 'negro')

print(f'{perro_nuevo.nombre} es de color {perro_nuevo.color}')
perro_nuevo.ladrar()
print(f'{perro_nuevo.nombre} tuvo un accidente y perdio 2 patas')


cerrar_ciclo = True
while cerrar_ciclo:
    perro_nuevo.alimentar()

    if not perro_nuevo.vivo:
        cerrar_ciclo = False
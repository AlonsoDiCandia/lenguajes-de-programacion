import random

class Perro:
    def __init__(self, nombre, raza, color):
        self.patas = 4
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.hambre = 10
        self.vivo = True
    
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
        # for e, alimento in enumerate(comidas):
        #     print(f'{e}.- {alimento}')
        
        alimento_escogido = input("Elija un alimento: ")

        self.hambre += comidas[alimento_escogido]

        print(f'{self.nombre} tiene {self.hambre} puntos de hambre')

        if self.hambre <= -50:
            self.vivo = False
    
    def ir_al_vet(self, curacion):
        print(f'{self.nombre} ha ido al veterinario')
        self.hambre += curacion

class Veterinario:
    def __init__(self):
        self.curacion = random.randint(1, 50)

perro1 = Perro('Carbonada', 'pug', 'negro')
vet1 = Veterinario()
# perro2 = Perro('Melon', 'Chiguagua', 'Rosa')

print(f'{perro1.nombre} es {perro1.raza} y es de color {perro1.color} y tiene {perro1.patas} patas')
# print(f'{perro2.nombre} es {perro2.raza} y es de color {perro2.color} y tiene {perro2.patas} patas')


# perro1.accidente(1)
# print(f'{perro1.nombre} tuvo un accidente y ahora tiene {perro1.patas} patas')

cerrar_ciclo = True
while cerrar_ciclo:
    perro1.alimentar()

    if not perro1.vivo:
        cerrar_ciclo = False

    if perro1.hambre < 0:
        perro1.ir_al_vet(vet1.curacion)
        if perro1.hambre < 0:
            print('ANDA A URGENCIAAA!')
        else:
            print(f'{perro1.nombre} ha sido curado')





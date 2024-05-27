import random
from random import choice

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.attack = random.randint(1, 10)
        self.deff = random.randint(1, 5)

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.__str__()

perros = []
nombres_para_perros = [
    "Fideo",
    "Chispa",
    "Galleta",
    "Taco",
    "Canelo",
    "Rumba",
    "Bolita",
    "Copito",
    "Mochi",
    "Zapato"
]

for _ in range(10):
    p = Perro(nombres_para_perros.pop())
    print(p)
    print(p.attack)
    perros.append(p)

perro1 = choice(perros)
perro2 = choice(perros)

while perro1.nombre == perro2.nombre:
    print('Hubo cambio de nombre')
    perro2 = choice(perros)

print(f'Va a pelear {perro1.nombre} vs {perro2.nombre}')

if perro1.attack > perro2.attack:
    print(f'{perro1.nombre} gana')
elif perro2.attack > perro1.attack:
    print(f'{perro2.nombre} gana')
else:
    print('Se mordieron pero nadie gano')
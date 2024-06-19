class Animal:
    def __init__(self):
        self.hambre = 20

    def nadar(self):
        print('Puedo nadar')

    def volar(self):
        print('Puedo volar')

    def correr(self):
        print('Puedo correr')
    
    def __comer(self):
        self.hambre -= 10
    
    def alimentarse(self):
        self.__comer()
        print(f'Mi hambre es {self.hambre}')

class Pez(Animal):
    def volar(self):
        print('No puedo volar :c')

    def correr(self):
        print('No puedo correr T.T')

class Perro(Animal):
    def volar(self):
        print('No puedo volar :c')

class Pato(Animal):
    pass

print('PEZ')
pez = Pez()
pez.nadar()
pez.volar()
pez.correr()
# pez.__comer()
pez.alimentarse()

print('PERRO')
perro = Perro()
perro.nadar()
perro.volar()
perro.correr()

print('Pato')
pato = Pato()
pato.nadar()
pato.volar()
pato.correr()

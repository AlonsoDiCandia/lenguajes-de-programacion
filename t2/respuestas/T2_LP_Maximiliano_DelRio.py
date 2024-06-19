import random

class Criatura:
    def __init__(self,nombre):
        self.nombre=nombre
        self.__vida=True
        self.__ataque=random.randint(1,25)
        self.__defensa=random.randint(1,100)
        self.__defensainicial=self.__defensa
    def __str__(self) -> str:
        return self.nombre
    
    def descanso(self):
        self.__defensa=self.__defensainicial

    def atacado(self,dañoataque):
        self.__defensa=self.__defensa-dañoataque
        if self.__defensa<=0:
            self.__vida=False

    def estado(self):
        return self.__vida
    
    def defensa(self):
        return self.__defensa
    
    def ataque(self):
        return self.__ataque
    
lista_de_criaturas=[]
personajes_criaturas = ["Vampiro", "Hombre Lobo", "Hada", "Demonio", "Elfo", "Centauro", "Ciclope", "Duende", 
                        "Troll", "Trauco", "Caleuche", "Pincoya", "Dragon", "Ogro", "Momia", "Cenicienta", 
                        "Blanca Nieves", "Rapunzel", "Enano", "Barbie", "Robot", "Herobrine", "Enderman", 
                        "Zombie", "Esqueleto", "Fantasma", "Bruja", "Sirena", "Gigante", "Banshee", "Kraken", "Yeti"]

peleadores=int(input("Ingrese cuantas criaturas quieres que peleen(2,4,8,16,32): "))
opciones=[2,4,8,16,32]
while peleadores not in opciones:
    peleadores=int(input("Ingrese cuantas criaturas quieres que peleen(2,4,8,16,32): "))
    
for _ in range(peleadores):
    c=Criatura(random.choice(personajes_criaturas))
    while c in lista_de_criaturas:
        c=Criatura(random.choice(personajes_criaturas))
    lista_de_criaturas.append(c)


### TORNEO ###
ronda=1
while len(lista_de_criaturas)!=1:
    print(f'##############Ronda {ronda}##############')
    for criatura in lista_de_criaturas:
        criatura.descanso()
    for i in range(len(lista_de_criaturas)//2):
        criatura1=lista_de_criaturas.pop()
        defensa1=criatura1.defensa()
        ataque1=criatura1.ataque()
        criatura2=lista_de_criaturas.pop()
        defensa2=criatura2.defensa()
        ataque2=criatura2.ataque()
        print(f'----Pelea {i+1} {criatura1} vs {criatura2}----')
        print(f"{criatura1} Ataque= {ataque1} Defensa={defensa1}")
        print(f"{criatura2} Ataque= {ataque2} Defensa={defensa2}")
        while criatura1.estado()==True or criatura2.estado()==True:
            if (defensa1 - ataque2)<=0:
                ganador=criatura2
                lista_de_criaturas.insert(0,ganador)
                break
            elif (defensa2 - ataque1) <=0:
                ganador=criatura1
                lista_de_criaturas.insert(0,ganador)
                break
            else:
                criatura2.atacado(ataque1)
                defensa2=defensa2-ataque1
                criatura1.atacado(ataque2)
                defensa1=defensa1-ataque2
        print(f'El ganador de esta ronda es {ganador}')
    ronda+=1
for criaturas in lista_de_criaturas:
    print(criaturas)


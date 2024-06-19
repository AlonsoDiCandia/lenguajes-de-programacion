import random
from random import randint

def fight(fighter1,fighter2): #el peleador 1 tiene preferencia
    if fighter1.total_defense <= 0:
        return fighter1
    elif fighter2.total_defense <= 0:
        return fighter2
    else:
        fighter2.vida = fighter2.modification(fighter1.atack)
        fighter1.vida = fighter1.modification(fighter2.atack)
        return fight(fighter1,fighter2)

class  criatura:
    def __init__(self,name):
        self.name = name
        self.vida = randint(1,101)
        self.defens = randint(0,51)
        self.atack = randint(1,71)
        self.total_defense = self.vida + self.defens

    def __str__(self):
        return self.name
    
    def modification(self,daño_recibido):
        self.total_defense -= daño_recibido
        return self.total_defense

peleadores_name = [
    "Guts",
    "Casca",
    "Skull Knight",
    "Griffith",
    "Ubik",
    "Zodd",
    "Rickert",
    "Void"
]
list_peleadores = []
for x in range(8):
    index = randint(0,len(peleadores_name)-1)
    name = peleadores_name[index]
    creat1 = criatura(name)
    peleadores_name.remove(name)
    list_peleadores.append(creat1)


cuartos = {}
for x in range(4):
    pelea1 = []
    fighter1 = list_peleadores.pop()
    fighter2 = list_peleadores.pop()
    pelea1.append(fighter1)
    pelea1.append(fighter2)
    cuartos[x+1] = pelea1

semis = []
for key,value in cuartos.items():
    name1 = value[0]
    name2 = value[1]
    semis.append(fight(name1,name2))


final = []   
for finalists in range(2):
    final.append(fight(semis[0],semis[1]))
    semis.remove(semis[0])
    #print(len(semis))
    if len(semis) > 1:
        semis.remove(semis[1])


winner = print(f'El gran campeon del torneo de criaturas de noche de viernes es {fight(final[0],final[1])}')


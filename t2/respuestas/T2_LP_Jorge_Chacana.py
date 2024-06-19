import random
class Criaturas:
    def __init__(self, nombre):
        self.vida = random.randint(100,800)
        self.ataque = random.randint(100, 200)
        self.defensa = random.randint(100,400)
        self.nombre = nombre
        
    def obtener_vida(self):
        return self.vida
    
    def mod_vida(self, nueva_vida):
        self.vida = nueva_vida

    def obtener_ataque(self):
        return self.ataque

    def mod_ataque(self, nuevo_ataque):
        self.ataque = nuevo_ataque

    def obtener_defensa(self):
        return self.defensa

    def mod_defensa(self, nueva_defensa):
        self.defensa = nueva_defensa
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return self.__str__()
    
lista_criaturas=[]
nom_criaturas = [
    'Gorila',
    'Mosca',
    'Donal Trump',
    'Rene Puentes',
    'Avestruz',
    'Michael Jackson',
    'Hormiga',
    'Skibidi Toilet',
    'Barack Obama',
    'Neandertal',
    'Nikola Tesla',
    'Elon Musk',
    'Mr. Tartaria',
    'Kim Jong-un',
    'Condorito',
    'Luffy',
    'Goku',
    'Loro',
    'Canguro',
    'Homero Simpson',
    'McLovin',
    'Walter White',
    'Mr. Beast',
    'Alexis Sanches',
    'Messi',
    'LeBron James',
    'Pablo Neruda',
    'Araña',
    'Oso',
    'Kurt Cobain',
    'Teutates Taranis',
    'Alonso Diaz Candia',
    'Azazel',
    'Peso Pluma',
    'Keanu Reeves',
    'Kenny McCormick'
]
while True:
    try:
        peleas = int(input("Cuantos combates quiere realizar (min: 2 - max: 32) en potencia de 2: "))
        if 2 <= peleas <= 32 and (peleas & (peleas - 1)) == 0:
            break
        elif peleas < 2 or peleas > 32:
            print('Tiene que ser dentro del rango 🤨' + '\n')
        else:
            print("Tiene que ser en potencia de 2 🤨" + '\n')
    except:
        print("Tiene que ser un numero 🤨" + '\n')

random.shuffle(nom_criaturas)
for _ in range(peleas):
    c = Criaturas(nom_criaturas.pop())
    lista_criaturas.append(c)
     
ronda = 1
while len(lista_criaturas) > 1:
    print(f"\nRonda {ronda}:")
    ganadores = []  

    for i in range(0, len(lista_criaturas), 2):
        criatura1 = lista_criaturas[i]
        criatura2 = lista_criaturas[i+1]
        #print(f'{criatura1.nombre} --- Vida {criatura1.obtener_vida()} --- Defensa {criatura1.obtener_defensa()} --- Ataque {criatura1.obtener_ataque()}')
        #print(f'{criatura2.nombre} --- Vida {criatura2.obtener_vida()} --- Defensa {criatura2.obtener_defensa()} --- Ataque {criatura2.obtener_ataque()}')

                
        while criatura1.obtener_vida() > 0 and criatura2.obtener_vida() > 0:
            if criatura2.obtener_defensa() > 0:
                if criatura1.obtener_ataque() >= criatura2.obtener_defensa():
                    criatura2.mod_defensa(0)
                else:
                    criatura2.mod_defensa(criatura2.obtener_defensa() - criatura1.obtener_ataque())
            else:
                criatura2.mod_vida(criatura2.obtener_vida() - criatura1.obtener_ataque())     
                      
            if criatura1.obtener_vida() > 0:
                if criatura1.obtener_defensa() > 0:
                    if criatura2.obtener_ataque() >= criatura1.obtener_defensa():
                        criatura1.mod_defensa(0)
                    else:
                        criatura1.mod_defensa(criatura1.obtener_defensa() - criatura2.obtener_ataque())
                else:
                    criatura1.mod_vida(criatura1.obtener_vida() - criatura2.obtener_ataque())
            
        if criatura1.obtener_vida() > 0:
            ganadores.append(criatura1)
        else:
            ganadores.append(criatura2)
            
        print(f"Combate: {criatura1} vs {criatura2} - Ganador: {ganadores[-1]}")
        
    lista_criaturas = ganadores
    ronda += 1


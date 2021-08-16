class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive=True
        self.ammo=5
        self.armor=60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

#######################
# Questão 1
#######################

listaTanques = []

# Inicializa lista com 5 tanques
for i in range(5):
    listaTanques.append(Tank("Tanque " + str(i)))

#######################
# Questão 2
#######################

import random

# Repete enquanto houver mais de um tanque na lista
while len(listaTanques) > 1:
    # Determina os indices
    indices = list(range(0,len(listaTanques)))

    # Escolhe aleatoriamente um atacante
    atacante = indices[random.randint(0, len(indices)-1)]

    # Remove o indice do atacante dos indices da lista
    indices.remove(atacante)

    # Escolhe aleatoriamente um defensor entre os atacantes
    defensor = indices[random.randint(0, len(indices)-1)]

    # Realiza o ataque
    listaTanques[atacante].fire_at(listaTanques[defensor])

    # Se o defensor morreu, remove da lista de tanques
    if not listaTanques[defensor].alive:
        listaTanques.remove(listaTanques[defensor])
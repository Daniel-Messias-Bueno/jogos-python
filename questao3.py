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
# Questão 3
#######################
import random

quantidade = 0
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
tanks = []
rodada = 1

# Le a quantidade de jogadores. Repete a leitura até obter um numero
# entre 2 e 10
while quantidade < 2 or quantidade > 10:
    print("Quantidade de tanques: ", end="")
    quantidade = int(input())

    if quantidade < 2 or quantidade > 10:
        print("Quantidade invalida!\n")

# Le os nomes dos jogadores
for i in range(0, quantidade):
    print("Nome do tanque " + str(i+1) + ": ", end="")
    nome = input()
    tanks.append(Tank(nome))

print() # Quebra a linha

# Determina o codigo dos jogadores a partir do alfabeto
jogadores = alfabeto[0:quantidade]

# Cria dicionario com os tanques
tanks = dict(zip(jogadores, tanks))

# Variavel separada para anotar a quantidade de tanques vivos
quantidade_vivos = quantidade

rolagem = [0]*quantidade
ordem = list(range(0,quantidade))

# Repete enquanto houver mais de 1 tanque vivo
while quantidade_vivos > 1:

    # Inicia a rodada
    print(">>> Rodada " + str(rodada) + ": jogando dados...")

    # Rola dados para cada jogador
    for i in range(quantidade):
        # Inicializa num igual a 0
        num = 0

        # Se o jogador da vez estiver vivo       
        if tanks.get(jogadores[i]).alive:
            # Rola uma numero de 1 a 6
            num = random.randint(1, 6)
            print(tanks.get(jogadores[i]).name + " rolou o número " + str(num) + "...")
        
        # Adiciona o numero à rolagem
        rolagem[i] = num

    # Estabelece nova ordem dos jogadores a partir da rolagem
    # Se houver empate, o jogador que atacou depois na rodada anterior,
    # agora ataca antes (essa regra não está no enuciado, mas o enunciado
    # não fala como lidar com o caso de empate nos dados)
    for i in range(0, quantidade-1):
        for j in range(i, quantidade):
            if rolagem[ordem[i]] <= rolagem[ordem[j]]:
                aux = ordem[j]
                ordem[j] = ordem[i]
                ordem[i] = aux

    # Faz a vez de cada jogador
    for vez in ordem:
        # Se o jogador da vez estiver vivo:
        if tanks.get(jogadores[vez]).alive:
            # Determina o tanque atacante
            atacante = tanks.get(jogadores[vez])
            print("\n" + atacante.name + " faz o ataque...")            
            
            # Inicializa flags para buscar jogador defensor
            defensor_existe = False
            defensor_vivo = False

            # Enquanto o defensor não existe ou não está vivo
            while not defensor_existe or not defensor_vivo:
                # Imprime a lista de tanques vivos, exceto o atacante
                print("Quem dejesa atacar?")
                for jogador in jogadores:
                    if jogador != jogadores[vez] and tanks.get(jogador).alive:
                        print(jogador + " - " + tanks.get(jogador).name)

                # Le a letra do tanque defensor
                print("Letra: ", end="")
                defensor_letra = input()

                # Reinicializa a flag, caso esteja na segunda iteração do loop
                defensor_existe = False
                defensor_vivo = False

                # Procura a letra na lista de tanques
                for jogador in jogadores:
                    # Se o tanque existir e não for o tanque atacante
                    if jogador != jogadores[vez] and jogador == defensor_letra:
                        # Altera a flag existe
                        defensor_existe = True
                        
                        # Se além de existir, o tanque estiver vivo
                        if tanks.get(defensor_letra).alive:    
                            # Altera a flag vivo
                            defensor_vivo = True

                # Se o tanque defensor não existe
                if not defensor_existe:
                    # Imprime tanque não encontrado
                    print("Tanque não encontrado!")
                # Se, pelo contrário, o tanque existe, mas não está mais vivo
                elif not defensor_vivo:
                    # Imprime que tanque nao está mais vivo
                    print("Tanque não está mais vivo!")
                
            # Após encontrar um defensor válido, encontra o tanque defensor
            defensor = tanks.get(defensor_letra)

            # Realiza o ataque
            atacante.fire_at(defensor)
        
            # Se o defensor morreu, diminui o numero de vivos
            if not defensor.alive:

                quantidade_vivos -= 1

    # Imprime detalhes de todos os jogadores
    print() # Quebra a linha
    for i in range(quantidade):
        print(tanks.get(jogadores[i]))

    print() # Quebra a linha
    
    # Incrementa o número de rodadas
    rodada += 1

# Após encerrar, imprime o nome do jogador que venceu
print(atacante.name + " venceu o jogo!")
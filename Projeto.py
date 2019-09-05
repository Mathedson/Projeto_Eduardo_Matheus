from numpy import random
class Pessoa:
    def __init__(self):
        self.ocupacao   = random.multinomial(100,[0.654 + random.uniform(-0.011,0.011),0.6])[0] #ocupado
        self.ensino     = random.multinomial(100,[0.22 + random.uniform(-0.0052,0.0052),0.6])[0] #publico
        self.sexo       = random.multinomial(100,[0.428 + random.uniform(-0.0095,0.0095),0.6])[0] #homem
        self.cor        = random.multinomial(100,[0.421 + random.uniform(-0.0115,0.0115),0.6])[0] #preto ou pardo
        self.modalidade = random.multinomial(100,[0.794 + random.uniform(-0.0505,0.0505),0.6])[0] #presencial
        self.classificacao()

    def classificacao(self):
        self.ocupacao = 'Ocupado' if self.ocupacao < random.uniform(0,100) else 'Não ocupado'
        self.ensino= 'Público' if self.ensino < random.uniform(0,100) else 'Privado'
        self.sexo= 'Homem' if self.sexo < random.uniform(0,100) else 'Mulher'
        self.cor = 'Preta ou parda' if self.cor < random.uniform(0,100) else 'Branca'
        self.modalidade = 'Homem' if self.modalidade < random.uniform(0,100) else 'À distância'

class Populacao:
    def __init__(self,tamanho = 1000):
        self.tamanho = tamanho
        self.individuos = []
        self.amostra(tamanho)

    def amostra(self,pop):
        for i in range(pop):
            self.individuos.append(Pessoa())

Pop=Populacao()
Pop.individuos

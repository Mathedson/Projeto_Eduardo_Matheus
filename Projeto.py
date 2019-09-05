from random import *
from numpy import *
class Pessoa():
    def __init__(self):
        self.modalidade = random.multinomial(100,[0.654 + random.uniform(-0.008,0.008),0.6])[0] #ocupado
        self.ensino     = random.multinomial(100,[0.22 + random.uniform(-0.081,0.081),0.6])[0] #publico
        self.sexo       = random.multinomial(100,[0.428 + random.uniform(-0.011,0.011),0.6])[0] #homem
        self.cor        = random.multinomial(100,[0.421 + random.uniform(-0.013,0.013),0.6])[0] #preto ou pardo
        self.modalidade = random.multinomial(100,[0.794 + random.uniform(-0.018,0.018),0.6])[0] #presencial
        self.classificacao()

    def classificacao(self):
        self.modalidade = 'Ocupado' if self.modalidade < random.uniform(0,100) else 'Não ocupado'
        self.ensino= 'Público' if self.modalidade < random.uniform(0,100) else 'Privado'
        self.sexo= 'Homem' if self.sexo < random.uniform(0,100) else 'Mulher'
        self.cor = 'Preta ou parda' if self.cor < random.uniform(0,100) else 'Branca'
        self.modalidade = 'Homem' if self.modalidade < random.uniform(0,100) else 'À distância'

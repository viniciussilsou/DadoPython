# criando dado em python

import random

class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Deseja gerar novo numero do dado ?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.GerarNumero()

    def GerarNumero(self):

        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()


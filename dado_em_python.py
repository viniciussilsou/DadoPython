# criando dado em python

import random

class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Deseja gerar novo numero do dado ?'

    def Iniciar(self):

        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarNumero()
            elif resposta == 'não' or resposta == 'n':
                print("Obrigado !")
            else:
                print("Favor Digitar sim ou não !")
        except:
            print("Ocorreu um erro ao executar o programa !")


    def GerarNumero(self):

        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()


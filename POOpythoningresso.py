class Ingresso():
    def __init__(self):
        self.valor=25

    def ImprimirValor(self):
        print(f'O valor do ingresso é {self.valor}')
class IngressoVip(Ingresso):
    def __init__(self):
        super().__init__()
        self.valor_adicional = 10
    def ImprimirValorVip(self):
        print(f'O valor impresso do ingresso vip é {self.valor} + {self.valor_adicional}, totalizando {self.valor+self.valor_adicional}')

jogo_futebol = IngressoVip()
jogo_futebol.ImprimirValorVip()
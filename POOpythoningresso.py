class Ingresso():
    def __init__(self,valor):
        self.valor=valor

    def ImprimirValor(self):
        print(f'O valor do ingresso é {self.valor}')

class IngressoVip(Ingresso):
    def __init__(self, valor,adicional):
        super().__init__(valor)
        self.adicional = adicional

    def ImprimirValorVip(self):
        print(f'O valor impresso do ingresso vip é {self.valor}+{self.adicional}, custando {self.valor+self.adicional}')


jogo_futebol = IngressoVip(25,15)
jogo_futebol.ImprimirValorVip()
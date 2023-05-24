class Atleta():
    def __init__(self,peso,aposentado=False):
        self.aposentado = aposentado
        self.peso = peso
        self.aquecido=False
    def Aposentar(self):
        if self.aposentado:
            print('O atleta já está aposentando!')
        else:
            print('O atleta foi aposentado!')
            self.aposentado=True
    def aquecer(self):
        if self.aposentado:
            print('Você não pode aquecer um atleta aposentado!')
        else:    
            if self.aquecido ==False:
                print('Atleta aquecido!')
                self.aquecido= True
            else:
                print('O atleta já está aquecido')
class Nadador(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    def Nadar(self):
        if self.aquecido:
            print('Seu atleta nadou!')
        else:
            print('Não se pode nadar sem aquecimento antes!')
    
class Ciclista(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    
    def Pedalar(self):
        if self.aquecido:
            print('O Atleta está pedalando!')
        else:
            print('Você precisa se aquecer antes de pedalar!')
class Corredor(Atleta):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)
    
    def Correr(self):
        if self.aquecido:
            print('O atleta correu!')
        else:
            print('Você não pode correr antes de se aquecer!')
class Triatleta(Corredor,Nadador,Ciclista):
    def __init__(self, peso, aposentado=False):
        super().__init__(peso, aposentado)

joao = Triatleta(50)
joao.aquecer()
joao.Correr()
joao.Nadar()
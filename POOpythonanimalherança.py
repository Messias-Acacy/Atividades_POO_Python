class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    
    def comer(self):
        print(f'O {self.nome} foi comer...')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    
    def Miar(self):
        print(f'O {self.nome} foi miando...')

class Cachorro(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def Latir(self):
        print(f'O {self.nome} Latiu...')

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    
    def Pular(self):
        print(f'O {self.nome} Pulou...')
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    
    def Muir(self):
        print(f'O {self.nome} muiu...')

animal_1 = Gato('cinzento','Azul')
print(vars(animal_1))

animal_1.Miar()
animal_1.comer()

animal_2 = Cachorro('gor','caramelo')
animal_2.Latir()
animal_2.comer()

animal_3 = Coelho('Floquinho','Branco')
animal_3.Pular()
animal_3.comer()

animal_4 = Vaca('Mimosa','Branca')
animal_4.Muir()
animal_4.comer()
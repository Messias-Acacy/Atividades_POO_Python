class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0
class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    
    def CalcularArea(self,base,altura):
        self.base= base
        self.altura = altura
        print(f'O calculo da área é: {self.base*self.altura}')
    
    def Perimetro(self):
        print(f'O calculo do perímetro é: {(self.base*2)+(self.altura*2)}')

class Triangulo(Forma):
    def __init__(self):
        super().__init__()
    def CalcularArea(self,base,altura):
        self.base = base
        self.altura = altura
        print(f'A área do triângulo é: {self.base*self.altura/2}')
    def Perimetro(self):
        print(f'O calculo do perímetro é: {self.area+(self.altura*2)}')


triangulo = Triangulo()
triangulo.CalcularArea(5,5)
quadrado = Retangulo()
quadrado.CalcularArea(5,5)


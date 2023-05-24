class Forma():
    def __init__(self,area,perimetro):
        self.area=area
        self.perimetro=perimetro
class Retangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)
    
    def CalcularArea(self):
        print(f'O calculo da área é: {self.area*self.area}')
    def Perimetro(self):
        print(f'O calculo do perímetro é: {self.perimetro*4}')

class Triangulo(Forma):
    def __init__(self, area, perimetro,altura):
        super().__init__(area, perimetro)
        self.altura = altura
    
    def CalcularArea(self):
        print(f'O calculo da área é: {self.area*self.altura/2}')
    def Perimetro(self):
        print(f'O calculo do perímetro é: {self.area+self.altura*2}')


triangulo = Triangulo(5,5,8)
triangulo.CalcularArea()
quadrado = Retangulo(5,5)
quadrado.CalcularArea()


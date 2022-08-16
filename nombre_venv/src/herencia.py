class Rectangulo:

    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura
    
    def area(self):
        return self.base*self.altura

class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(base = lado, altura = lado)


class Inmobiliario:
    def __init__(self, paredes, suelo, tamanno, plantas):
        self.paredes = paredes
        self.suelo = suelo 
        self.tamanno = tamanno
        self.plantas = plantas

class Casa(Inmobiliario):
    def __init__(self,luz, agua, gas):
        super().__init__(paredes = 4, suelo = True, tamanno = 90, plantas = 2)
        self.agua = agua 
        self.gas = gas 
        self.luz = luz 

class Cocina(Casa):
    def __init__(self, nevera, vitro, bombillo):
        super().__init__(luz = True, agua = True, gas = True)
        self.nevera = nevera 
        self.vitro = vitro 
        self.bombillo = bombillo 
        self.tamanno /=3
    
class Mi_cocina(Cocina):
    def __init__(self, microondas, lavavajilla, ):
        super().__init__(nevera = True, vitro = True, bombillo = 5)
        self.microondas = microondas
        self.lavavajilla = lavavajilla


if __name__ == "__main__":
    mi_cocina = Mi_cocina(microondas = True, lavavajilla = True)
    print(mi_cocina.suelo)
    print(mi_cocina.bombillo)
    print(mi_cocina.paredes)
    print(mi_cocina.tamanno)
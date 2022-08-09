#Objeto automovil 

class Automovil:
    def __init__(self, modelo, marca, color)
        self.modelo = modelo 
        self.marca = marca 
        self.color = color 
        
        #variables privadas
        self._estado = "En reposo"
        self._motor: Motor = None

    def acelerar(self, tipo = "despacio"):
        if tipo == "rapida":
            self._motor.inyecta_gasolina
        else:
            self._motor.inyecta_gasolina
        
        self._estado = "En Movimiento"

class Motor:
    def __init__(self, cilindros, tipo = "gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo 
        self._temperatura = None 
    
    def inyecta_gasolina(self, cantidad):
        pass 

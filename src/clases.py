#Definición de una clase 

from unicodedata import name


class Mi_class:
    #Constructor - Propiedades
    def __init__(self):
        pass

    #Metodos 
    def metodos_de_clase(self, argumentos):
        pass

class Persona():
    def __init__(self, nombre, edad):
        self.edad = edad 
        self.nombre = nombre 
    
    def saluda(self, otra_persona):
        return f"Hola {otra_persona} me llamo {self.nombre}"

    #Convención - Propiedades privadas
    _hola = lambda self: f"Hola {self.name}"


    


david = Persona("David", 22)
print(david.saluda("Luis"))
print(david.nombre)

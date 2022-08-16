from distutils.command.install_egg_info import safe_name


class Millas:
    distancia = 0 

    #Getter
    @property
    def obtener_distancia(self):
        return self.distancia

    #setter    
    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError ("La distancia no puede ser negativa")
        else:
            self.distancia = valor 

avion = Millas()

avion.distancia = 100 

print(avion.definir_distancia)


class Perros(object): #Declaramos la clase principal Perros
    def __init__(self, nombre): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos (privados ocultos)
    
    @property
    def nombre(self): #Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla" # Doc del método
        return self.__nombre #Aquí simplemente estamos retornando el atributo privado oculto
#Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.

#Ahora vamos a utilizar setter y deleter para modificarlos
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print (f"El nombre se ha modificado por {self.__nombre}") #Aquí vuelvo a pedir que retorne el atributo para confirmar
    
    @nombre.deleter #Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
        
        #Hasta aquí property#

saanvi = Perros("Sananvi")
print(saanvi.nombre)
saanvi.nombre = "Saanvi"
print(saanvi)
del saanvi.nombre
saanvi.nombre = "luis"
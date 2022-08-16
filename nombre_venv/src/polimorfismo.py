class Deportista:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    def ficha_deportista(self):
        print(f"el deportista se llama {self.nombre} y su edad es {self.edad}")

class Futbolista(Deportista):
    def __init__(self, nombre, edad, deporte):
        super().__init__(nombre, edad)
        self.deporte = deporte
    
    def ficha_deportista(self):
        print(f"el deportista se llama {self.nombre}, su edad es {self.edad} y realiza el deporte {self.deporte}")


def run():
    futbolista = Futbolista("Luis", 37, "futbol").ficha_deportista()
    

if __name__ == "__main__":
    run()

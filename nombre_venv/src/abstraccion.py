class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura = "caliente"):
        self._llenar_tanque(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    #Esto es un metodo privado
    def _llenar_tanque(self, temperatura):
        print(f"llenando el tanque con agua{temperatura}")

    def _anadir_jabon(self):
        print("Añadiendo jabon")

    def _lavar(self):
        print("Lavando la ropa")
    
    def _centrifugar(self):
        print("Añadiendo jabon")




#Ejemplo

class Televisor():
    def __init__(self):
        pass
    
    def _ver_tele(self):
        self._control_remeto()
        self._reproducir_canal()
        self._volumen_establecido()
    
        

    def _control_remeto(self):
        boton_encendido = self._encender()
        canal = self._escoger_canal_numero()
        cambiador = self._cambiar_canal()
        volumen = self.cambiar_volumen()

    
    def _reproducir_canal(self):
        canal_elegido = self._escoger_canal_numero()
        print(f"Mostrando contenido del canal {canal_elegido}")


    
    def _escoger_canal_numero(self, num1 = input("Introduce un canal: "), num2 = input("Introduce un canal: ")):
        canal_elegido = num1 + num2
        print(f"el canal seleccionado es: {canal_elegido}")
        return int(canal_elegido)

    def _encender(self):
        print(f"el televisor esta encendido")

    def _cambiar_canal(self):
        cambiador = input("¿Canal anterior o siguiente?: ")
        if cambiador == "siguiente":
            up = self._escoger_canal_numero()
            up += 1
            return up
        else:
            down = self._escoger_canal_numero()
            down -= 1
            return down

    def _cambiar_volumen(self):
        camb_volumen = int(input("Introduce un numero: "))
        print(f" el nuevo volumen del televisor es: {camb_volumen} ")



if __name__ == "__main__":
    Televisor = Televisor()
    Televisor._control_remeto()
    Televisor._ver_tele()
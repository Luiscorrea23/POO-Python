def funcion_decoradora(funcion): 
    def encapsular():
        print("Primer mensaje")
        funcion()
        print("segundo mensaje")
    
    return encapsular
    
def saluda():
    print(f"hola Luis")

saludar = funcion_decoradora(saluda)
saludar()

saluda()
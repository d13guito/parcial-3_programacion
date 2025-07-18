# Apagado y encendido de una lampara usando OOP
class Lampara:
    def __init__(self):
        self.encendida = False  # Estado inicial
class Lampara:
    def __init__(self):
        self.encendida = False  # Estado inicial

    def encender(self):
        self.encendida = True
        print("Lámpara encendida")

    def apagar(self):
        self.encendida = False
        print("Lámpara apagada")

lampara = Lampara()
lampara.encender()

#salida
#Lámpara encendida

class Lampara:
    def __init__(self):
        self.encendida = False  # Estado inicial

    def encender(self):
        self.encendida = True
        print("Lámpara encendida")

    def apagar(self):
        self.encendida = False
        print("Lámpara apagada")

lampara = Lampara()
lampara.apagar()

#salida
#Lámpara apagada

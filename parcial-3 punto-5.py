#definicion

#clase padre
Vehículo (tiene 2 cosas):
Atributo: ruedas = 4
Método: avanzar ()

#clase hija
AutoF1 (hereda de Vehículo y añade):
Atributo extra: velocidad_Max = 320 km/h
Método extra: DRS ()

#casos de uso

#creacion de paguinas webs
<div style="border:1px solid #ccc;padding:10px;width:200px;text-align:center;">
  <img src="https://via.placeholder.com/150" style="width:100%;">
  <h3>Camiseta Retro</h3>
  <p>$49.900</p>
  <button>Comprar</button>
</div>

#programacion de aplicaciones moviles

class Mascota(val nombre: String) {
    fun saludar() {
        println("Hola, me llamo $nombre")
    }
}

fun main() {
    val mascota = Mascota("Maggie")
    mascota.saludar()
}

#programacion de videojuegos
para computador), el codigo de objetos en estos programas se pueden ver de la siguiente manera.

public class Mascota {
    public string nombre;

    public Mascota(string nombre) {
        this.nombre = nombre;
    }

    public void Saludar() {
        Debug.Log("Hola, soy " + nombre);
    }
}

#parte practica

#ejemplo 1

class Computador:
    Disco_solido = True

if __name__ == '__main__':


class Computador:
    Disco_solido = True

if __name__ == '__main__':
    computador_1 = Computador()

class Computador:
    disco_solido = True

if __name__ == '__main__':
    computador_1 = Computador()
    print(computador_1.disco_solido)

#salida True
class Lampara:
    def __init__(self):
        self.encendida = False  # Estado inicial

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def mostrar_estado(self):
        if self.encendida:
            print("La lámpara está encendida")
        else:
            print("La lámpara está apagada")


#Ejemplo 2

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


class Vehiculo:

    def __init__(self, transmision=str, color=str):
        self.transmision = transmision
        self.color = color

    def avanzar(self, nivel_gasolina=int):
        """
        Creamos una función que recibe un parámetro de tipo int
        Si el nivel de gasolina es mayor a 0, el vehiculo avanza
        """
        if nivel_gasolina != 0:
            print("Estoy avanzando")
        else:
            print("No puedo avanzar")

class Carro(Vehiculo):

    def __init__(self, transmision, color, puertas=int):
        super().__init__(transmision, color)
        self.puertas = puertas

class Moto(Vehiculo):

    def __init__(self, transmision, color, llantas=int):
        super().__init__(transmision, color)
        self.llantas = llantas


if __name__ == "__main__":
    versa = Carro(transmision="manual", color="gris", puertas=4)
    versa.avanzar(nivel_gasolina=100)

    italika = Moto(transmision="manual", color="naranja", llantas=2)
    italika.avanzar(nivel_gasolina=0)
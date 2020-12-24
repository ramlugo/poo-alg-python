
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print("Estoy caminando")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print("Estoy moviéndome en mi bicicleta")


def main():
    persona = Persona("David")
    persona.avanzar()

    ciclista = Ciclista("Daniel")
    ciclista.avanzar()


if __name__ == "__main__":
    main()
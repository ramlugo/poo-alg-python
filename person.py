def run():
    # Definimos una clase "Persona"
    class Persona:

        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self, otra_persona):
            return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'


    # Así se usa nuestra clase persona
    david = Persona('David', 35)
    ramses = Persona('Ramses', 21)

    david.saludar(ramses)

if __name__ == "__main__":
    run()
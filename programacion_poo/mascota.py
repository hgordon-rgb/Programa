# Definición de la clase Mascota

class Mascota:
    
    # Constructor (atributos)
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # Método para mostrar información
    def mostrar_informacion(self):
        print("\n Información de la Mascota ")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")

    # Método para simular sonido
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido...")
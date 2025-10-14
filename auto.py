from enum import Enum

class Combustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CIUDAD = "Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
        else:
            self.velocidad_actual = self.velocidad_maxima

    def frenar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            self.velocidad_actual = 0

    def imprimir(self):
        print("Marca:", self.marca)
        print("Modelo (año):", self.modelo)
        print("Motor:", f"{self.motor} L")
        print("Tipo de Combustible:", self.tipo_combustible.value)
        print("Tipo de Automóvil:", self.tipo_automovil.value)
        print("Número de puertas:", self.numero_puertas)
        print("Cantidad de asientos:", self.cantidad_asientos)
        print("Velocidad máxima:", f"{self.velocidad_maxima} km/h")
        print("Color:", self.color.value)
        print("Velocidad actual:", f"{self.velocidad_actual} km/h")
        print("--------------------------------------")

# Método main
if __name__ == "__main__":
    auto1 = Automovil("Toyota", 2022, 1.8, Combustible.GASOLINA,
                      TipoAutomovil.COMPACTO, 4, 5, 200, Color.ROJO)

    auto2 = Automovil("Ford", 2021, 2.0, Combustible.DIESEL,
                      TipoAutomovil.SUV, 5, 7, 220, Color.NEGRO)

    auto1.imprimir()
    auto2.imprimir()

    print("Probando acelerar y frenar en el Toyota:")
    auto1.acelerar(50)
    auto1.imprimir()
    auto1.frenar(20)
    auto1.imprimir()

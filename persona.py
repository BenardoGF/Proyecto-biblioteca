class Persona:
    def __init__(self, nombre, apellido, documento_identidad, anio_nacimiento, pais_nacimiento, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.documento_identidad = documento_identidad
        self.anio_nacimiento = anio_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero  # 'H' para hombre, 'M' para mujer

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Documento: {self.documento_identidad}")
        print(f"Año de Nacimiento: {self.anio_nacimiento}")
        print(f"País de Nacimiento: {self.pais_nacimiento}")
        print(f"Género: {'Hombre' if self.genero == 'H' else 'Mujer'}")
        print("--------------------------------------")


# Método main para probar la clase
if __name__ == "__main__":
    # Crear dos personas
    persona1 = Persona("Carlos", "Ramírez", "12345678", 1990, "México", 'H')
    persona2 = Persona("María", "López", "87654321", 1995, "Colombia", 'M')

    # Imprimir sus datos
    persona1.imprimir()
    persona2.imprimir()

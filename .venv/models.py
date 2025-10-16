from dataclasses import dataclass, field

# Clase para representar un libro
@dataclass
class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def mark_borrowed(self):
        """Marca el libro como prestado"""
        if not self.available:
            raise ValueError("El libro ya está prestado.")
        self.available = False

    def mark_returned(self):
        """Marca el libro como disponible otra vez"""
        self.available = True


# Clase para representar un miembro de la biblioteca
@dataclass

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
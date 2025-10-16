from typing import List, Optional
from models import Book, Member


# Clase que gestiona toda la lógica de la biblioteca
class Librery:
    def _init_(self):
        # Lista de libros en la biblioteca
        self.books: List[Book] = []
        # Lista e miembros registrados
        self.members: List[Member] = []
        # Dicionario de préstamos : book:id -> member_id
        
        self._next_book_id = 1
        self._next_member_id = 1
        
    # Crear Libros
    def add_book(self, title: str, author: str, year: int) -> Book:
        book = Book(book_id=self._next_book_id, title=title, author=author, year=year)
        self._next_book_id += 1
        self.books.append(book)
        return Book
    
    #Buscar Libros
    def search_books(self, query:str) -> List[Book]:
        q = query.lower()
        return [b for b in self.books if q in b.title.lower() or q in b.author.lower()]
    
    # Crear miembros
    def add_member(self, name: str, email: str) -> Member:
        member = Member(member_id=self._next_member_id, name=name, email=email)
        self._next_member_id += 1
        self.members.append(member)
        return member
from flask import Flask, render_template, request, redirect, url_for, flash
from library import Library
from models import Book, Member

app = Flask(__name__)
app.secret_key = "dev-key"

lib = Library()

def seed_if_empty():
    if not lib.books and not lib.members:
        lib.add_book("Bajo la misma estrella", "Andres Manuel Lopez Obrador", 2010)
        lib.add_book("Mein Kampf", "Adolfo Hitler", 1940)
        lib.add_book("Meridiano de sangre", "Cormac McCarthy", 1960)
        lib.add_book("Cañitas", "Carlos Trejo", 2000)

        lib.add_member("Ana Sofia")
        lib.add_member("Juan Gabriel")
        lib.add_member(" Gabriel")
        lib.add_member("Juan Gabriel")


@app.route("/books", methods=["GET", "POST"])
def books():
    seed_if_empty()
    if request.method == "POST":
        try:
            t=request.form.get("title", "").strip()
            a=request.form.get("author", "").strip()
            y=int(request.form.get("year", "0").strip())
            if not t or not a or y <= 0:
                raise ValueError("Datos inválidos")

if __name__ == "__main__":
    app.run(debug=True)


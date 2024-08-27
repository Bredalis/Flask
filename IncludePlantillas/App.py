
from flask import Flask, render_template

app = Flask(__name__)

articulos = [
    {"Nombre": "Mouse", "Cantidad": 5},
    {"Nombre": "Monitor", "Cantidad": 2},
    {"Nombre": "Teclado", "Cantidad": 3}
]

@app.route("/")
def index():
    return render_template("index.html", titulo = "Mi Sitio Web")

@app.route("/Tienda")
def tienda():
    return render_template("Tienda.html", nombre = "Juan", 
        direccion = "Av. Manuela Díez", empleados = ["Juanito", "Sofia", "Marta"],
        articulos = articulos)

@app.route("/Articulos")
def lista_articulos():
    return render_template("Articulos.html", articulos = articulos)

if __name__ == "__main__":
    app.run()
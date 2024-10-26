
from flask import Flask, render_template

app = Flask(__name__)

# Lista de artículos disponibles en la tienda
articulos = [
    {"Nombre": "Mouse", "Cantidad": 5},
    {"Nombre": "Monitor", "Cantidad": 2},
    {"Nombre": "Teclado", "Cantidad": 3}
]

# Ruta para la página principal
@app.route("/")
def index():
    return render_template("index.html", titulo = "Mi Sitio Web")

# Ruta para la página de la tienda
@app.route("/tienda")
def tienda():
    return render_template("Tienda.html", 
        nombre = "Juan", 
        direccion = "Av. Manuela Díez",
        empleados = ["Juanito", "Sofia", "Marta"],
        articulos = articulos)

# Ruta para la lista de artículos
@app.route("/articulos")
def lista_articulos():
    return render_template("Articulos.html", articulos = articulos)

if __name__ == "__main__":
    app.run(debug = True)
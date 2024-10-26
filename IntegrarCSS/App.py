
from flask import Flask, render_template

app = Flask(__name__)

# Lista de usuarios con nombres y biografías
usuarios = [
    ("Juan", "Nació el 25 de Junio del 2000"), 
    ("Chris", "Nació el 15 de Abril del 1999"),
    ("Pedro", "Nació el 6 de Octubre del 2008")
]

@app.route("/")
def inicio():
    return render_template("index.html", usuarios = usuarios)

@app.route("/<nombre_usuario>")
def perfil_usuario(nombre_usuario):
    # Buscar el usuario por nombre
    usuario_encontrado = next((usuario for usuario in usuarios if usuario[0] == nombre_usuario), None)

    if not usuario_encontrado:
        return render_template("404.html"), 404

    # Mostrar la información del usuario
    return render_template("Perfil.html", usuario = usuario_encontrado)

if __name__ == "__main__":
    app.run(debug = True)
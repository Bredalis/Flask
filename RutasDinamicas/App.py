
from flask import Flask, render_template

app = Flask(__name__)

usuarios = [
    ("Juan", "Nacio el 25 de Junio del 2000"), 
    ("Chris", "Nacio el 15 de Abril del 1999"),
    ("Pedro", "Nacio el 6 de Octubre del 2008")
]

@app.route("/")
def inicio():
    return render_template("index.html", usuarios = usuarios)

@app.route("/<nombre_usuario>")
def perfil_usuario(nombre_usuario):
    usuario_encontrado = None

    for usuario in usuarios:
        if usuario[0] == nombre_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        return render_template("404.html")

    print(usuario_encontrado)

    return render_template("Perfil.html", usuario = usuario_encontrado)

if __name__ == "__main__":
    app.run()
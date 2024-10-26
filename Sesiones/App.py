
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "bredalis2013"

usuarios = {}

@app.route("/")
def index():
    usuario = session.get("nombre")

    if usuario:
        return f"Bienvenido {usuario} a la app de registro de usuarios"
    return f"Bienvenido a la app de registro de usuarios"

@app.route("/registro", methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["nombre"]
        contraseña = request.form["contraseña"]

        session["nombre"] = usuario
        usuarios[usuario] = contraseña

        print(usuarios)
        return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/cerrar-sesion")
def cerrar_sesion():
    session.pop("nombre", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
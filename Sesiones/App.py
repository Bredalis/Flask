
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "bredalis2013"

usuarios = {}
print(usuarios)

@app.route("/")
def index():
    usuario = session.get("usuario")

    if usuario:
        return f"Bienvenido {usuario} a la app de registro de usuarios"
    return f"Bienvenido a la app de registro de usuarios"

@app.route("/Registro", methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        session["usuario"] = usuario
    
        usuarios[usuario] = contraseña
        print(usuarios)
        return redirect(url_for("index"))

    return render_template("index.html")

@app.route("/Cerrar_Seccion")
def cerrar_seccion():
    session.pop("usuario", None)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
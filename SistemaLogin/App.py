
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "bredalis2013"

usuarios = {}
print(usuarios)

@app.route("/")
def index():
    usuario = session.get("Usuario")

    if usuario:
        return f"Bienvenido {usuario} a la app de registro de usuarios"
    return f"Bienvenido a la app de registro de usuarios"

@app.route("/Registro", methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        if usuario in usuarios and usuarios[usuario] == contraseña:
            return "Ya estas registrado"

        else:
            session["Usuario"] = usuario
        
            usuarios[usuario] = contraseña
            print(usuarios)
            return redirect(url_for("index"))

    return render_template("index.html")

@app.route("/Acceso", methods = ["GET", "POST"])
def acceso():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]

        if usuario in usuarios and usuarios[usuario] == contraseña:

            session["Usuario"] = usuario
            return redirect(url_for("index"))

        else:
            return "Nombre de usuario o contraseña incorrecta"

    return render_template("Acceso.html")

@app.route("/Cerrar_Seccion")
def cerrar_seccion():
    session.pop("Usuario", None)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
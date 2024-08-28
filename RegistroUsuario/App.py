
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = {}
print(usuarios)

@app.route("/")
def index():
    return "Bienvenido a la app de registro de usuarios"

@app.route("/Registro", methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"]
    
        usuarios[usuario] = contraseña
        print(usuarios)
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
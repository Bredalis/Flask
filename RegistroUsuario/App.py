
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diccionario para almacenar los usuarios y sus contraseñas
usuarios = {}

@app.route("/")
def index():
    return "Bienvenido a la app de registro de usuarios"

@app.route("/registro", methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        # Recupera el nombre de usuario y la contraseña del formulario
        usuario = request.form["nombre"]
        contraseña = request.form["contraseña"]
    
        # Almacena el usuario y la contraseña en el diccionario
        usuarios[usuario] = contraseña
        print("Usuarios registrados", usuarios)

        # Redirige a la página de inicio
        return redirect(url_for("index"))

    # Renderiza el formulario de registro en caso de petición GET
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
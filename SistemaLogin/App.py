
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "bredalis2013" # Clave secreta para manejar sesiones

# Diccionario para almacenar usuarios y contraseñas
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

         # Validar si el usuario ya está registrado
        if usuario in usuarios:
            return "Ya estas registrado"

        # Registrar y almacenar la sesión del nuevo usuario
        session["nombre"] = usuario
        usuarios[usuario] = contraseña
        print(usuarios)

        return redirect(url_for("index"))
    return render_template("index.html") # Renderizar formulario de registro

@app.route("/acceso", methods = ["GET", "POST"])
def acceso():
    if request.method == "POST":
        usuario = request.form["nombre"]
        contraseña = request.form["contraseña"]

        # Validar credenciales de acceso
        if usuarios.get(usuario) == contraseña:
            session["nombre"] = usuario
            return redirect(url_for("index"))

        return "Nombre de usuario o contraseña incorrecta"
    return render_template("Acceso.html") # Renderizar formulario de acceso

@app.route("/cerrar-sesion")
def cerrar_sesion():
    session.pop("nombre", None) # Cerrar sesión del usuario actual
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
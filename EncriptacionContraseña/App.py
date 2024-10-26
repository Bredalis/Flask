
from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = "bredalis2013"

# Diccionario para almacenar usuarios 
# y contraseñas encriptadas
usuarios = {}
print(usuarios)

@app.route("/")
def index():
    usuario = session.get("Usuario")

    if usuario:
        return f"Bienvenido {usuario} a la app de registro de usuarios"
    return f"Bienvenido a la app de registro de usuarios"

@app.route("/registro", methods = ["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = pbkdf2_sha256.hash(request.form["contraseña"]) # Encriptar la contraseña

        if usuario in usuarios and usuarios[usuario] == contraseña:
            return "Ya estas registrado"

        else:
            session["Usuario"] = usuario

            # Guardar el usuario y su contraseña encriptada        
            usuarios[usuario] = contraseña
            print(usuarios)
            return redirect(url_for("index"))

    return render_template("index.html")

@app.route("/acceso", methods = ["GET", "POST"])
def acceso():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contraseña = request.form["contraseña"] 

        # Verificar si el usuario existe y la contraseña es correcta
        if usuario in usuarios and pbkdf2_sha256.verify(contraseña, usuarios[usuario]):

            session["Usuario"] = usuario
            return redirect(url_for("index"))

        else:
            return "Nombre de usuario o contraseña incorrecta"

    return render_template("Acceso.html")

@app.route("/cerrar-sesion")
def cerrar_sesion():
    session.pop("Usuario", None)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)
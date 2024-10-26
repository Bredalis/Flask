
from flask import Flask, render_template

# Instancia de la app y cambio del nombre del directorio static
app = Flask(__name__, static_folder = "Estaticos")

# Ruta para la página principal 
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para la página de Login
@app.route("/login")
def login():
    return render_template("Login.html")

# Ruta para la página de Signup
@app.route("/ruta/sign-up")
def signup():
    return render_template("Signup.html")

if __name__ == "__main__":
    app.run(debug = True)
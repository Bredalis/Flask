
from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

# Punto de entrada para ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug = True)
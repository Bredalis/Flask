
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route("/", methods = ["GET", "POST"])
def obtener_datos():
	nombre = request.form.get("nombre") if request.method == "POST" else None
	return render_template("index.html", nombre = nombre)

if __name__ == "__main__":
	app.run(debug = True)
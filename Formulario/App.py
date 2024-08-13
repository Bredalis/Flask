
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def obtener_datos():
	info_formulario = ""

	if request.method == "POST":
		info_formulario = request.form.get("contenido")

	return render_template("index.html", nombre = info_formulario)

if __name__ == "__main__":
	app.run()
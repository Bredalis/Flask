
from flask import Flask, render_template

# Instancia de la app
app = Flask(__name__)

@app.route("/variables")
def template_variable():
	return render_template("index.html", nombre = "Lisa", curso = "Flask")

# Ejecutar la app
if __name__ == "__main__":
	app.run(debug = True)

from flask import Flask, render_template

# Instancia
app = Flask(__name__)

@app.route("/variables")
def template_variable():
	return render_template("index.html", nombre = "Lisa", curso = "Flask")

# Poder ejecutarlo directamente desde el editor
if __name__ == "__main__":
	app.run()

from flask import Flask, render_template

# Instancia
app = Flask(__name__)

@app.route("/")
def saludo():
	return "Hola, Mundo"

@app.route("/nuevo contenido")
def nuevo_contenido():
	return """

		<html>
		<head>
			<title>Flask</title>
		</head>
		<body>
			<h1>Mi primer programa con Flask y Python en la Web</h1>
		</body>
		</html>
	"""

# Unir la pagina de html
@app.route("/index")
def template_index():
	return render_template("index.html")

# Poder ejecutarlo directamente desde el editor
if __name__ == "__main__":
	app.run()
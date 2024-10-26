
from flask import Flask, render_template

def crear_app():
	app = Flask(__name__)

	# Ruta principal que renderiza index.html
	@app.route("/")
	def saludo():
		return render_template("index.html")

	return app

if __name__ == "__main__":

	# Crear instancia de la aplicación y ejecutar
	app = crear_app()
	app.run()
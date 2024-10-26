
from flask import Flask, render_template

# Instancia de la app
app = Flask(__name__)

class Peliculas:
	def __init__(self, nombre, año, protagonista):
		self.nombre = nombre
		self.año = año
		self.protagonista = protagonista

@app.route("/estructura")
def estructura_de_datos():
	peliculas = [
		"El lobo de Wall Street",
		"Harry Potter",
		"Volver al Futuro"
	]

	pelicula_lobo = {
		"Nombre": "El lobo de Wall Street",
		"Año": 2013,
		"Protagonista": "Leonardo DiCaprio"
	} 

	# Instancia de la clase
	pelicula_volver = Peliculas("Volver al Futuro", "1895", "Michael J.")

	return render_template("index.html", peliculas = peliculas, 
		diccionario = pelicula_lobo, clase = pelicula_volver)

if __name__ == "__main__":
	app.run(debug = True)
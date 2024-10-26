
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Conexión a la base de datos MongoDB
cliente = MongoClient(os.getenv("CLAVE_MONGO"))
app.db = cliente["Formulario"]
coleccion = app.db["Usuarios"]

# Ruta principal que maneja GET y POST
@app.route("/", methods = ["GET", "POST"])
def obtener_datos():

	# Obtener los usuarios
	usuarios = {usuario["Nombre"] for usuario in coleccion.find({})}
	nombre = request.form.get("nombre")

	if request.method == "POST" and nombre not in usuarios:
		coleccion.insert_one({"Nombre": nombre})
		usuarios.add(nombre)

		print(usuarios) # Mostrar los usuarios

	return render_template("index.html", usuarios = usuarios)

if __name__ == "__main__":
	app.run(debug = True)
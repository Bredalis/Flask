
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)

# Conectar la bbdd 
cliente = MongoClient(os.getenv("CLAVE_MONGO"))
app.db = cliente["Formulario"]
coleccion = app.db["Usuarios"]

# Obtener los usuarios
usuarios = [usuario["Nombre"] for usuario in coleccion.find({})]

@app.route("/", methods = ["GET", "POST"])
def obtener_datos():
	info_formulario = request.form.get("contenido")

	if request.method == "POST" and info_formulario != "":
		parametro = {"Nombre": info_formulario}
		
		coleccion.insert_one(parametro)
		usuarios.append(info_formulario)

		print(usuarios) # Mostrar los usuarios

	return render_template("index.html", usuarios = usuarios)

if __name__ == "__main__":
	app.run()
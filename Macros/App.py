
from flask import Flask, render_template

app = Flask(__name__)

# Definición de usuarios y sus roles
usuarios = [
	("Julio", "Admin"), ("Perla", "Usuario"), 
	("Claribel", "Usuario"), ("Julian", "Admin")
]

usuarios_2 = [
	("Raul", "Admin"), ("Mario", "Usuario"), 
	("Bella", "Usuario"), ("Kris", "Admin")
]

@app.route("/")
def lista_usuarios():
	return render_template("index.html", usuarios = usuarios, 
		usuarios_2 = usuarios_2)

if __name__ == "__main__":
	app.run(debug = True)
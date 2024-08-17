
from flask import Flask, render_template

app = Flask(__name__)

usuarios = ["Luis", "Jhon", "Diego"]

@app.route("/")
def lista_usuarios():
	return render_template("index.html", usuarios = usuarios)

if __name__ == "__main__":
	app.run()
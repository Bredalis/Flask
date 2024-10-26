
from flask import Flask, render_template

# Instancia de la app
app = Flask(__name__)

@app.route("/condicionales")
def condicional():
	return render_template("index.html", grupo = "BTS")

if __name__ == "__main__":
	app.run(debug = True)
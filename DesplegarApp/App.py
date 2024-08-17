
from flask import Flask, render_template
from dotenv import load_dotenv

def crear_app():
	app = Flask(__name__)

	@app.route("/")
	def saludo():
		return render_template("index.html")
	return app

if __name__ == "__main__":
	app = crear_app()
	app.run()

from flask import Flask, render_templates

app = Flask(__name__)

usuarios = [
    ("Juan", "Nacio el 25 de Junio del 2000"), 
    ("Chris", "Nacio el 15 de Abril del 1999"),
    ("Pedro", "Nacio el 6 de Octubre del 2008")
]

# @app.route("/")


if __name__ == "__main__":
    app.run()

from flask import Flask, render_template

# Instancia de la app
app = Flask(__name__)

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)
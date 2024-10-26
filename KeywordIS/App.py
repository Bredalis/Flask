
from flask import Flask, render_template

app = Flask(__name__)

# Variable de ejemplo
variable = (1, 2, 3, 4)

@app.route("/")
def index():
    return render_template("index.html", variable = variable)

if __name__ == "__main__":
    app.run(debug = True)
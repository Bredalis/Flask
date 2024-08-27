
from flask import Flask, render_template

app = Flask(__name__, static_folder = "Estaticos")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Login")
def login():
    return render_template("Login.html")

@app.route("/ruta/SignUp")
def signup():
    return render_template("Signup.html")

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template

app = Flask(__name__)

# Código HTML que se inyectará en las plantillas
html = """
    <div>
        <p>Esto es un <strong>ejemplo</strong>.</p>
    </div>
"""

@app.route("/")
def index():
    return render_template("index.html", html = html)

@app.route("/jinja2")
def index_jinja2():
    return render_template("index.jinja2", html = html)

if __name__ == "__main__":
    app.run(debug = True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/ciclo for")
def ciclo_for():

	grupos_masculinos = [
		"BTS", 
		"Seventeen",
		"Stray Kids",
		"NCT",
		"TXT",
		"Enhypen"
	]

	grupos_femeninos = {
		1: "BlackPink",
		2: "Twice",
		3: "NewJeans",
		4: "BabyMonster",
		5: "Itzy",
		6: "Ive"
	}	

	return render_template("index.html", grupos_masculinos = grupos_masculinos,
		grupos_femeninos = grupos_femeninos)

if __name__ == "__main__":
	app.run()
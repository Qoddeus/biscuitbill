# IMPORTS
from flask import Flask, render_template, url_for


# CONFIGURATIONS
app = Flask(__name__)


# SETS in LIST
players = [
	# STARTERS
	{ "ht": "6-8", "wt": "230", "image": "mf.png", "numero": "31", "player": "VIN", "plays": "SF|PF", "point": "Forward" },
	{ "ht": "6-6", "wt": "250", "image": "jd.png", "numero": "27", "player": "JULES", "plays": "SG|SF", "point": "Guard" },
	{ "ht": "6-5", "wt": "200", "image": "pl.png", "numero": "00", "player": "PAT", "plays": "SG|PG", "point": "Guard" },
	{ "ht": "6-11", "wt": "300", "image": "rg.png", "numero": "24", "player": "RODRIGO", "plays": "C", "point": "Center" },
	{ "ht": "6-10", "wt": "280", "image": "af.png", "numero": "00", "player": "GELO", "plays": "PF|SF", "point": "Forward" },

	# BENCH
	{ "ht": "6-3", "wt": "220", "image": "vl.png", "numero": "00", "player": "VHON", "plays": "PG|SG", "point": "Guard" },
	{ "ht": "6-8", "wt": "999", "image": "ep.png", "numero": "34", "player": "ETHAN", "plays": "SF|SG", "point": "Forward" },
	{ "ht": "6-6", "wt": "101", "image": "mp.png", "numero": "00", "player": "MAKO", "plays": "SG", "point": "Guard" },
	{ "ht": "6-6", "wt": "220", "image": "tt.png", "numero": "65", "player": "THADZ", "plays": "SF", "point": "Forward" }
]


# ROUTES
@app.route("/")
def biscuithome():
	return render_template("biscuitbill.html", players=players)


# ERROR HANDLERS
@app.errorhandler(403)
def error_403(error):
	return render_template("errors/403.html"), 403

@app.errorhandler(404)
def error_404(error):
	return render_template("errors/404.html"), 404

@app.errorhandler(500)
def error_500(error):
	return render_template("errors/500.html"), 500


# RUN APP
if __name__ == "__main__":
	app.run()

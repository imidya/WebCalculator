# import web
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route("/login", methods=['GET'])
def login():
	if request.method == 'GET':
		return render_template("login.html")

@app.route("/ezCalculator", methods=['GET'])
def ezCalculator():
	if request.method == 'GET':
		return "This is ezCalculator page"


if __name__ == "__main__":
    app.run()
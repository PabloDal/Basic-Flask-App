import flask
from savedata import *
from flask import request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#renders index page with cat variable
@app.route('/', methods=['GET'])
def home():
	cat = []
	for i in dataset:
		a = i["category"]
		cat.append(a)
	cat = set(cat)
	return render_template("index.html", cat=cat)

#renders category page with data variable, requires an entry
@app.route('/category', methods=['POST', 'GET'])
def api_all():
	query = request.form['Category']
	data = []
	for i in dataset:
  		if i["category"] == query:
  			data.append(i)

	return render_template("category.html", data = data)

app.run()
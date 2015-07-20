from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'name': 'Conor'}
	return render_template('index.html', title='Home', user=user)

@app.route('/results')
def results():
	user = {'name': 'Conor'}
	results = [{'name':'Result 1'}, {'name':'Result 2'}, {'name':'Result 3'}]
	return render_template('results.html', title='Home', user=user, results=results)

from app import app
from flask import render_template
import utils

@app.route('/')
@app.route('/index')
def index():
	user = {'name': 'Conor'}
	return render_template('index.html', title='Home', user=user)

@app.route('/results')
def results():
	distance = request.args.get('dist') if request.args.get('dist') != None else 10
	coordinates = (request.args.get('lat'), request.args.get('long'))
	user = {'name': 'Conor'}
	results = [{'name':'Result 1', 'latitude': -70.909343, 'longitude': 34.76876}, {'name':'Result 2', 'latitude': 39.67, 'longitude': 75.61}, {'name':'Result 3', 'latitude': 42.37, 'longitude': -71.25}]
	results = filterToLocation(results, coordinates, distance)
	return render_template('results.html', title='Home', user=user, results=results)

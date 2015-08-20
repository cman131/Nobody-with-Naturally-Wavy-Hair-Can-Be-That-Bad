from app import app, models
from flask import render_template, request
import math

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Conor'}
    return render_template('index.html', title='Home', user=user)

@app.route('/results')
def results():
    distance = request.args.get('dist') if request.args.get('dist') != None else 10
    coordinates = (
        request.args.get('lat') if request.args.get('lat') != None else 70.909333,
        request.args.get('long') if request.args.get('long') != None else 34.768463)
    user = {'name': 'Conor'}
    models.Park.query.all()
    results = filterToLocation(results, coordinates, distance)
    return render_template('results.html', title='Home', user=user, results=results)


# Non routes

def filterToLocation(listy, coordinates, distance=10):
    newListy = []
    phi1 = (90 - coordinates[0]) * math.pi/180
    theta1 = coordinates[1] * math.pi/180
    for i in listy:
        phi2 = (90 - i.latitude) * math.pi/180
        theta2 = i.longitude * math.pi/180
        cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) + math.cos(phi1) * math.cos(phi2))
        actualDist = 3959 * math.acos(cos)
        if(actualDist <= distance):
            i.distance = actualDist
            newListy.append(i)
    return newListy

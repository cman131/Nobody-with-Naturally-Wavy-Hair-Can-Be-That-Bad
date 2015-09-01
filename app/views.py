from app import app, models, config
from flask import render_template, request, jsonify
import math, urllib.request, json

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Conor'}
    return render_template('index.html', title='Home', user=user)

@app.route('/results')
def results():
    distance = request.args.get('dist')
    coordinates = (
        request.args.get('lat') if request.args.get('lat') != None else 70.909333,
        request.args.get('long') if request.args.get('long') != None else 34.768463)
    user = {'name': 'Conor'}

    results = models.Park.all()
    if(distance!=None):
        results = filterToLocation(results, coordinates, distance)
    return render_template('results.html', title='Results', user=user, results=results)

@app.route('/park')
def park():
    if(request.args.get('id')==None):
        return jsonify({'status': 500})
    user = {'name': 'Conor'}
    park = models.Park.get(request.args.get('id'))
    return render_template('park.html', title=park.name, user=user, config=config, parky=park.__dict__())


@app.route('/park/create')
def create():
    if(request.args.get('name')==None):
        return 'A 500 error occurred.'

    # Retrieve lat and long from google
    locationData = urllib.request.urlopen(config.GEOCODE_API_BASE_URL +
        '?address='+request.args.get('address').replace(' ', '+') + ',' +
        request.args.get('city').replace(' ', '+') + ',' +
        request.args.get('state') + '&key=' + config.GEOCODE_API_KEY).read()
    locationData = json.loads(locationData.decode('utf-8'))['results'][0]['geometry']['location']

    # Make a temporary object with the given data and save it to the db
    temp = models.Park(None, request.args.get('name'),
                    request.args.get('size'),
                    request.args.get('address'),
                    request.args.get('zip_code'),
                    request.args.get('state'),
                    request.args.get('city'),
                    int(request.args.get('playground')),
                    float(locationData['lat']),
                    float(locationData['lng']))
    return jsonify({'status': 200 if temp.save() else 500})

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

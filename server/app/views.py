from app import app, models, config, tabletop_generator
from flask import render_template, redirect, request, jsonify, json, Response
import math, requests, json

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Conor', 'id': 1}
    return render_template('index.html', title='Home', user=user)

@app.route('/deck')
def deck():
    if(request.args.get('id') == None):
        return jsonify({'status': 400, 'message': 'Bad id. Go home, you\'re clearly drunk.'})
    try:
        int(request.args.get('id'))
    except Exception:
        return jsonify({'status': 400, 'message': 'Bad id. Go home, you\'re clearly drunk.'})

    deck = models.Deck.get(request.args.get('id'))
    if(deck == None):
        return jsonify({'status': 404, 'message': 'Deck not found.'})
    return jsonify({'status': 200, 'deck': deck.__dict__()})

@app.route('/decks')
def decks():
    decks = models.Deck.search(request.args.get('searchTerm'))
    return jsonify({'status': 200, 'results': decks})

@app.route('/deck/tabletop')
def deckTabletop():
    if(request.args.get('id') == None):
        return jsonify({'status': 400, 'message': 'Bad id. Go home, you\'re clearly drunk.'})
    try:
        int(request.args.get('id'))
    except Exception:
        return jsonify({'status': 400, 'message': 'Bad id. Go home, you\'re clearly drunk.'})
    deck = models.Deck.get(request.args.get('id'))
    if(deck == None):
        return jsonify({'status': 404})
    cards = deck.getDetailedCardList() + deck.getSideboard()
    outputJson = tabletop_generator.TableTopGenerator.generateTableTopJson(deck.name, 'Generated deck', cards)
    return Response(outputJson,
             mimetype='application/json',
             headers={'Content-Disposition': 'attachment;filename='+deck.name.replace(' ', '_')+'.json'})

@app.route('/deck/create', methods=['POST'])
def create():
    if('name' not in request.json or 'author' not in request.json or 'cards' not in request.json):
        return jsonify({'status': 400, 'missing': 'name, author, or cards'})

    # Make a temporary object with the given data and save it to the db
    cards = request.json['cards']
    sideboard = []
    if ('sideboard' in request.json):
        sideboard = request.json['sideboard']
    temp = models.Deck(None, request.json['name'], request.json['author'], cards, sideboard)
    status = temp.save()
    return jsonify({'status': 200 if status else 400, 'id': temp.id})

@app.route('/deck/update', methods=['PUT'])
def update():
    if('id' not in request.json or 'name' not in request.json or 'cards' not in request.json):
        return jsonify({'status': 400, 'missing': request.json})
    try:
        int(request.json['id'])
    except Exception:
        return jsonify({'status': 400, 'message': 'Bad id. Go home, you\'re clearly drunk.'})

    deck = models.Deck.get(int(request.json['id']))
    if deck is None:
        return jsonify({'status': 404})

    # Make a temporary object with the given data and save it to the db
    cards = request.json['cards']
    sideboard = []
    if ('sideboard' in request.json):
        sideboard = request.json['sideboard']
    temp = models.Deck(deck.id, request.json['name'], request.json['author'], cards, sideboard)
    status = temp.save()
    return jsonify({'status': 200 if status else 500, 'id': temp.id})

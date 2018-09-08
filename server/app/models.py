from app import dbconnect
from app import config
from flask import json

cursor, connection = dbconnect.connection(config)

class Card:
    def __init__(self, id, name, description, types, imageUrl, cmc, power, toughness):
        self.id = id
        self.name = name
        self.description = description
        self.imageUrl = imageUrl
        self.type = types
        self.cmc = cmc
        self.power = power
        self.toughness = toughness

    def save(self):
        try:
            data = [self.id, self.name, self.description, self.type, self.imageUrl, int(self.cmc), self.power, self.toughness]
            command = ('INSERT INTO Card (id, name, description, type, imageUrl, cmc, power, toughness) ' +
                        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s);')
            cursor.execute(command, data)
            connection.commit()
        except Exception:
            return self.name
        return ''

    @staticmethod
    def load(id):
        data = [id]
        command = ('SELECT * FROM Card WHERE id=%s;')
        cursor.execute(command, data)
        result = cursor.fetchall()[0]
        return Card(id, result['name'], result['description'], result['type'], result['imageUrl'], result['cmc'], result['power'], result['toughness'])

    @staticmethod
    def clear(yaSure):
        if yaSure=='DOIT':
            command = ('DELETE FROM Card WHERE id!=%s')
            cursor.execute(command, ['0'])
            connection.commit()

class Deck:
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    cards = FOREIGN
    sideboard = FOREIGN
    """

    def __init__(self, id, name, author, cards=[], sideboard=[]):
        self.id = id
        self.name = name
        self.author = author
        self.cards = cards
        self.sideboard = sideboard

    def __dict__(self):
        return {'id': self.id,
                'name': self.name,
                'author': self.author,
                'cards': self.cards,
                'sideboard': self.sideboard}

    def __repr__(self):
        return '<Deck %r>' % self.name

    def getDetailedCardList(self):
        command = ('SELECT Card.*, Deck_Card.count FROM Card '
                   'JOIN Deck_Card on Card.id=Deck_Card.cardid '
                   'WHERE Deck_Card.deckid=%s;')
        cursor.execute(command, [self.id])
        cards = cursor.fetchall()
        multipliedCards = []
        for card in cards:
            for i in range(0, card['count']):
                multipliedCards.append(card)
        return multipliedCards
    
    def getSideboard(self):
        command = ('SELECT Card.*, Side_Card.count FROM Card '
                   'JOIN Side_Card on Card.id=Side_Card.cardid '
                   'WHERE Side_Card.deckid=%s;')
        cursor.execute(command, [self.id])
        cards = cursor.fetchall()
        multipliedCards = []
        for card in cards:
            for i in range(0, card['count']):
                multipliedCards.append(card)
        return multipliedCards

    def save(self):
        data = [self.name, self.author]
        command = ('INSERT INTO Deck (name, author) VALUES (%s, %s);')
        if(self.id != None):
            data.append(int(self.id))
            command = ('UPDATE Deck SET name=%s, author=%s WHERE id=%s;')
        cursor.execute(command, data)
        connection.commit()
        self.id = self.id if self.id != None else cursor.lastrowid
        if self.cards != []:
            command1 = ('DELETE FROM Deck_Card WHERE deckId=%s;')
            data1 = [self.id]
            command2 = ''
            data2 = []
            cardSet = {}
            for card in self.cards:
                power = None;
                toughness = None;
                if 'power' in card:
                    power = card['power']
                if 'toughness' in card:
                    toughness = card['toughness']
                tempCard = Card(card['id'], card['name'], card['description'], card['type'], card['imageUrl'], card['cmc'], power, toughness)
                tempCard.save()
                if card['id'] not in cardSet:
                    cardSet[card['id']] = 1
                else:
                    cardSet[card['id']] += 1
            command2 = 'INSERT INTO Deck_Card (deckId, cardId, count) VALUES'
            for key,value in cardSet.items():
                command2 += ' (%s, %s, %s),'
                data2.append(self.id)
                data2.append(key)
                data2.append(value)
            command2 = (command2[:-1] + ';')
            cursor.execute(command1, data1)
            cursor.execute(command2, data2)
            connection.commit()
        if self.sideboard != []:
            command1 = ('DELETE FROM Side_Card WHERE deckId=%s;')
            data1 = [self.id]
            command2 = ''
            data2 = []
            cardSet = {}
            for card in self.sideboard:
                power = None;
                toughness = None;
                if 'power' in card:
                    power = card['power']
                if 'toughness' in card:
                    toughness = card['toughness']
                tempCard = Card(card['id'], card['name'], card['description'], card['type'], card['imageUrl'], card['cmc'], power, toughness)
                tempCard.save()
                if card['id'] not in cardSet:
                    cardSet[card['id']] = 1
                else:
                    cardSet[card['id']] += 1
            command2 = 'INSERT INTO Side_Card (deckId, cardId, count) VALUES'
            for key,value in cardSet.items():
                command2 += ' (%s, %s, %s),'
                data2.append(self.id)
                data2.append(key)
                data2.append(value)
            command2 = (command2[:-1] + ';')
            cursor.execute(command1, data1)
            cursor.execute(command2, data2)
            connection.commit()
        return True

    #Static Methods

    @staticmethod
    def all():
        cursor.execute('SELECT * FROM Deck;')
        return cursor.fetchall()

    @staticmethod
    def get(deckId):
        cursor.execute('SELECT * FROM Deck WHERE id=%s;', [int(deckId)])
        results = cursor.fetchall()
        if len(results) <= 0:
            return None
        result = results[0]
        deck = Deck(deckId, result['name'], result['author'])
        deck.cards = deck.getDetailedCardList()
        deck.sideboard = deck.getSideboard()
        return deck

    @staticmethod
    def search(term):
        command = """SELECT Deck.id, Deck.name, Deck.author, cards.count as cardCount, sides.count as sideCount FROM Deck 
                  LEFT JOIN (Select deckId, COALESCE(SUM(count), 0) AS count FROM Deck_Card GROUP BY deckId) cards ON cards.deckId = Deck.id
                  LEFT JOIN (Select deckId, COALESCE(SUM(count), 0) AS count FROM Side_Card GROUP BY deckId) sides ON sides.deckId = Deck.id;"""
        data = []
        if (term != None):
            term = '%'+term+'%'
            command = command[:-1] + ' WHERE Deck.name like %s OR Deck.author like %s;'
            data = [term, term]
        cursor.execute(command, data)
        results = cursor.fetchall()
        for result in results:
            result['cardCount'] = 0 if result['cardCount'] == None else int(result['cardCount'])
            result['sideCount'] = 0 if result['sideCount'] == None else int(result['sideCount'])
        return results

from app import dbconnect
from app import config

cursor, connection = dbconnect.connection(config)

class Park():
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    size = db.Column(db.String(45))
    address = db.Column(db.String(45))
    zip_code = db.Column(db.String(45))
    state = db.Column(db.String(45))
    city = db.Column(db.String(45))
    playground = db.Column(db.Integer)
    latitude = db.Column(db.Float(11, 8))
    longitude = db.Column(db.Float(11, 8))
    """

    def __init__(self, id, name, size, address, zip_code, state, city,
                playground, latitude, longitude):
        self.id = id
        self.name = name
        self.size = size
        self.address = address
        self.zip_code = zip_code
        self.state = state
        self.city = city
        self.playground = playground
        self.latitude = latitude
        self.longitude = longitude

    def __dict__(self):
        return {'id': self.id,
                'name': self.name,
                'size': self.size,
                'address': self.address,
                'zip_code': self.zip_code,
                'state': self.state,
                'city': self.city,
                'playground': self.playground,
                'latitude': self.latitude,
                'longitude': self.longitude}

    def get(id):
        cursor.execute('SELECT * FROM Park WHERE id=' + id + ';')
        result = cursor.fetchall()[0]
        return Park(id, result['name'],
        result['size'],
        result['address'],
        result['zip_code'],
        result['state'],
        result['city'],
        result['playground'],
        float(result['latitude']),
        float(result['longitude']))

    def all():
        cursor.execute('SELECT * FROM Park;')
        return cursor.fetchall()

    def save(self):
        data = [self.name, self.size, self.address, self.zip_code, self.state,
                self.city, int(self.playground), float(self.latitude),
                float(self.longitude)]
        print(len(data))
        command = ('INSERT INTO Park (name, size, address, '
                    'zip_code, state, city, playground, latitude, longitude) '
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);')
        if(self.id != None):
            data.append(int(self.id))
            command = ('UPDATE Park SET name=%s'
                        ', size=%s'
                        ', address=%s'
                        ', zip_code=%s'
                        ', state=%s'
                        ', city=%s'
                        ', playground=%s'
                        ', latitude=%s'
                        ', longitude=%s'
                        ' WHERE id=%s;')
        cursor.execute(command, data)
        connection.commit()
        return True

    def __repr__(self):
        return '<Park %r>' % (self.name)

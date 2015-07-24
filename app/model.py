from app import db

class Park(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    size = db.Column(db.String(45))
    address = db.Column(db.String(45))
    zip_code = db.Column(db.String(45))
    state = db.Column(db.String(45))
    city = db.Column(db.String(45))
    playground = db.Column(db.Integer)

    def __repr__(self):
        return '<Park %r>' % (self.name)

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + app.config['MYSQL_DATABASE_USER'] + ':' + app.config['MYSQL_DATABASE_PASSWORD'] + '@' + app.config['MYSQL_DATABASE_HOST']
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    size = db.Column(db.String(45))
    address = db.Column(db.String(45))
    zip_code = db.Column(db.String(45))
    state = db.Column(db.String(45))
    city = db.Column(db.String(45))
    playground = db.Column(db.Integer)



"""
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST']
mysql.init_app(app)
connection = mysql.connect()
cursor = connection.cursor()

data = cursor.fetchall()

if len(data) is 0:
    conn.commit()
    return json.dumps({'message':'User created successfully !'})
else:
    return json.dumps({'error':str(data[0])})
"""

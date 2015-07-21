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

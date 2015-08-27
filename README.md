# MakeFriendsYouCanCallByNicknamesEvenWhenYouAreOld
A Python Flask web application to rate Parks in your area


<h1>How to set up and run</h1>
<h3>Windows</h3>
 1. You need to first install <a href='https://www.python.org/downloads/'>python 3.4.x</a> (x means I don't care which :D )
 2. You will also need to <a href='https://docs.python.org/3/using/windows.html'>set up your PATH</a>
 3. Now we need to install a few things so open cmd or gitBash as admin and run these commands:

 ```
python -m pip install flask
python -m pip install flask-login
python -m pip install flask-openid
python -m pip install flask-mail
python -m pip install flask-sqlalchemy
python -m pip install sqlalchemy-migrate
python -m pip install flask-whooshalchemy
python -m pip install flask-wtf
python -m pip install flask-babel
python -m pip install guess_language
python -m pip install flipflop
python -m pip install coverage
 ```
 4. You also need to install and <a href'http://dev.mysql.com/downloads/windows/installer/'>set up mysql</a>
 5. Now you need to go <a href='https://developers.google.com/maps/documentation/geocoding/intro'>get yourself a key</a> for google's geocoding api
 6. Navigate to where you have cloned this project
   6.1. If you have not yet, follow the recommended git setup section or just do it how you want.
 7. Now make a copy of the config_example.py file named 'config.py'
 8. Now fill the user, password, and api_key variables with what you have from setting up mysql
 ```
import os
basedir = os.path.abspath(os.path.dirname(__file__))

GEOCODE_API_KEY = "dis here's a key"
GEOCODE_API_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

MYSQL_DATABASE_USER = "iamtotallyavalidusername"
MYSQL_DATABASE_PASSWORD = "lookatmeimapassword"
MYSQL_DATABASE_DB = "ParkRater"
MYSQL_DATABASE_HOST = "localhost"
 ```
 <h5 style='color: red'>WARNING: Do NOT ever commit your config information</h5>
 <p>this would make them public knowledge</p>

 9. Now run the dbSetup.py with ```python dbSetup.py```
 10. If all went well you should now be able to run ```python run.py``` to start the server on <a href='http://localhost:5000'>localhost:5000</a>


<h1>Recommended Git Setup</h1>
1. Fork this project on github
2. Make sure you have <a href='https://git-scm.com/book/en/v2/Getting-Started-Installing-Git'>git installed</a>.
3. Now go ahead and open a terminal or git bash if on windows.
4. Navigate to the directory you want this project to be in.
5. Now execute ```git clone https://github.com/{GitUsername}/MakeFriendsYouCanCallByNicknamesEvenWhenYouAreOld.git```
  5.1 replace {GitUsername} with your git username
6. The remaining command is to set the remote ```git add remote upstream https://github.com/cman131/MakeFriendsYouCanCallByNicknamesEvenWhenYouAreOld.git```

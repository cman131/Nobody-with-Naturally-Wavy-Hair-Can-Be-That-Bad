
getUrl = app.config['GEOCODE_API_BASE_URL'] + '?sensor=false&key=' + app.config['GOOGLE_SERVER_API_KEY'] + '&address=' + address.split(' ').join('+')

latitude = float(response['results'][0]['geometry']['location']['lat'])
longitude = float(response['results'][0]['geometry']['location']['lng'])

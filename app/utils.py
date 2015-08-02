import Math

def filterToLocation(listy, coordinates, distance):
    newListy = []
    for i in listy:
        latDiff = (i.latitude - coordinates[0]) * Math.pi/180
        longDiff = (i.longitude - coordinates[1]) * Math.pi/180
        diffTan = Math.sin(latDiff/2)** + Math.sin(longDiff/2)** + Math.cos(coordinates[0]*Math.pi/180) * Math.cos(i.latitude*Math.pi/180)
        actualDist = 6371000 * Math.atan2(Math.sqrt(diffTan), Math.sqrt(1-diffTan)) * 2
        if(Math.sqrt(actualDist**2) <= distance):
            newListy.append(i)

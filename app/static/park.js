function setMap(){
    coords = document.getElementById('coordinates');
    latitude = parseInt(coords.innerHTML.split(', ')[0]);
    longitude = parseInt(coords.innerHTML.split(', ')[1]);
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: latitude, lng: longitude},
        zoom: 18,
        height: 250,
        width: 250
    });
}

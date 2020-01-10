import geocoder
g = geocoder.ip('me')
lat, lon = str(g.latlng[0]), str(g.latlng[1])

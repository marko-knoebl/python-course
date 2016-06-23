# download the JSON data for London

import urllib2
import json

url = 'http://api.openweathermap.org/data/2.5/weather?q=Vienna&appid=76a06be0de6d6cb054d5110c719ef51b'

weather_string = urllib2.urlopen(url).read()

weather = json.loads(weather_string)

print weather['clouds']['all']
print weather['main']['temp']

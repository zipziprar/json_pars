import json
from urllib.request import urlopen


url = urlopen('https://raw.githubusercontent.com/zemirco/sf-city-lots-json/master/citylots.json')
obj = json.load(url)
data = [street for street in obj['features'] if street['properties']['STREET'] == 'JEFFERSON']
data = sorted(data, key=lambda k: k['properties']['LOT_NUM'], reverse=True)
print(data)

'some changes'
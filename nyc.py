import requests
import csv

url = 'https://data.cityofnewyork.us/api/views/7vgu-qbur/rows.csv?date=20241206&accessType=DOWNLOAD'
r = requests.get(url)
d = r.text
d = d.split(',')
print(len(d))

import requests
import json
import pandas as pd

url = 'https://www.7timer.info/bin/api.pl?lon=121.474&lat=31.23&product=civil&output=json'
r = requests.get(url)
text_j = json.loads(r.text)
wether_info = pd.DataFrame(text_j['dataseries'])
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)
pd.set_option('display.max_colwidth', 1000)
start_time = pd.to_datetime(text_j['init'], format='%Y%m%d%H')
wether_info['timepoint'] = pd.to_timedelta(wether_info['timepoint'], unit='h')
wether_info['timestamp'] = start_time + wether_info['timepoint']
print(wether_info.head(5))

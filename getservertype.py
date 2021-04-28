#!usr/bin/python3

import requests

URL = 'http://google.com'
re = requests.get(URL)
status = str(re.status_code)
print('Status Code: ' + status)
print('Server type: ' + re.headers['Server'])

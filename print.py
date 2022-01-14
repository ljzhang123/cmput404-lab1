import requests

print('\nrequests library version: ' + requests.__version__)

response = requests.get(url='http://www.google.com/')
print('google.com GET status code: %i' % response.status_code)
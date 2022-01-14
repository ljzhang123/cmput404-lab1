import requests

print(open(__file__).read())

download = requests.get(url='https://raw.githubusercontent.com/ljzhang123/cmput404-lab1/master/print.py')
open('downloaded-script.py', 'wt').write(download.text)

print('\nrequests library version: ' + requests.__version__)

response = requests.get(url='http://www.google.com/')
print('google.com GET status code: %i' % response.status_code)
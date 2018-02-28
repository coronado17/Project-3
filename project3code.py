from urllib.request import urlopen
import time

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
response = urlopen(url)

logfile = response.read().decode('utf-8').split('\n')

from urllib.request import urlopen
import time

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
response = urlopen(url)

logfile = response.read().decode('utf-8').split('\n')

#will have count by day for week/month
count_dict = {}
Fourxx_error = 0
Threexx_error = 0
# count for unique request file
request_file = {}
# saves last actual month
lastmonth = 0
# file variable (for open and write data to file) that allows to write data by month
currentfile = None
total = 0

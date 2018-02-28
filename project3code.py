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

for log in httpfile:
    log = log.split()
    if len(log) == 10:
      total += 1
    #parse date using strptime()method
    date = time.strptime(log[3][1:]), '%d/%b/%Y:%H:%M:%S')
    #number of week
    week = int(time.strftime("%U", date))
    
    
    # write log file by month
    if date.tm_mon == lastmonth:
      # write log in current file
      currentfile.write(' '.join(log) + '\n')
    else:
      if currentfile:
        currentfile.close()
    #open new file
    currentfile = open(time.strftime("%b", date), 'a')
    #if last month is equal to current 
    lastmonth = date.tm_mon
    
    #log by day for week&month
    if count_dic.get(tm_mon):
      #current month/week check
      if count_dic.get[date.tm_mon].get(week):
        #if true check day
        if count_dic[date.tm_mon][week].get(date.tm_mday):
          count_dic[date.tm_mon][week][date.tm_mday] += 1
        #if week doesnt have current month
        else:
          count_dic[date.tm_mon ][week][date.tm_mday] = 1
      #month doesnt have current week
      else:
        count_dic[date.tm_mon][week] = {date.tm_mday: 1}
    else:
      count_dic[date.tm_mon] = {week: {date.tm_mday: 1}}
      
    if 400 <= int(log[8]) < 500:
      Fourxx_error += 1
    if 300 <= int(log[8]) < 400:
      Threexx_error += 1
    if requestfile.get(log[6]):
      requestfile[log[6]] += 1
    else:
      requstfile[log[6]]= 1

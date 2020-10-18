import time, getopt, sys
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="12.0.0.1"

argumentList = sys.argv[1:]
websitelist = map(lambda s: 'www.'+s+'.com',argumentList)
#countseconds = 0
while True:
    #countseconds+=1
    #print(countseconds)
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() and dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours")
        with open(hosts_path, '+r') as file:
            content = file.read()
            for website in websitelist:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websitelist):
                    file.write(line)
            file.truncate()
        print("Productive Hours")
        print('Following website have been blocked:',','.join(websitelist))
    #print(1)
    time.sleep(5)

from datetime  import datetime as dt
import time
localhost="127.0.0.1"
temp="hosts"
host = "C:\\Windows\\System32\\drivers\\etc\\hosts" #r ath the begining
website=["facebook.com",'www.facebook.com','www.instagram.com']


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        with open(host,'r+') as file:
            content = file.read()
            for web in website:
                if web in content:
                    pass
                else:
                    file.write("\n"+localhost+"  "+web)

    else:
        with open(host,'r+') as file:
            content = file.readlines()
            file.seek(0)
            file.truncate()
            for lines  in content:
                if not any(web in lines for web in website):
                    file.write(lines)
    time.sleep(5)

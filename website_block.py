import datetime as dt
import time

end_time = dt.datetime(2023,8,15) #kaab taak block karni hai
site_block = ["www.instagram.com","www.facebook.com"]
host_path = "enter path of host for macbook"
redirect = "127.0.0.1" #localhost from computer

while True:
    if dt.datetime.now()<end_time:
        print("start Blocking")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                  if website not in content:
                        host_file.write("\n"+website+" "+redirect+"\n")
                  else:
                        pass
    else:
         with open(host_path,"r+") as host_file:
              content = host_file.readlines()
              host_file.seek(0)
              for lines in content:
                   if not any(website in lines for website in site_block):
                        host_file.write(lines)

                        host_file.truncate()
                        time.sleep(5)
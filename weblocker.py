import datetime
import time

end_time = datetime.datetime(2024,3,6)
site_block = ["www.youtube.com", "www.w3schools.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Start blocking")
        with open(host_path, "r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect + " " + website + "\n")
                else:
                    pass
    else:
        with open(host_path, "r+") as host_file:
            content = host_file.readline()
            host_file.seek(0)
            for line in content:
                if not any(website in line for website in site_block):
                    host_file.write(line)
            host_file.truncate()
        time.sleep(5)


# open cmd -> run as adminstrator
# write following command
# cd..
# cd..
# cd web
# yourfilename.py
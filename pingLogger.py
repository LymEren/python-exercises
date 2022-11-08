# The program pinging in pingHost.txt file

import requests
from datetime import datetime

pingList = {
    "URL": [],
    "Response": [],
    "Result": []
}

urlCounter = int(input("How many URLs do you want to ping?: "))

for value in range(urlCounter):
    pingInput = input(f"Enter the {value + 1}. URL you want to ping: ")
    pingList["URL"].append("http://" + pingInput)

for value in range(urlCounter):
    if requests.get(pingList["URL"][value]).status_code == 200:
        pingList["Response"].append(requests.get(pingList["URL"][value]).status_code)
        pingList["Result"].append("UP")
    elif requests.get(pingList["URL"][value]).status_code == 500:
        pingList["Response"].append(requests.get(pingList["URL"][value]).status_code)
        pingList["Result"].append("DOWN")

    with open('pingHost.txt', 'a') as pLog:
        pLog.write("{} - URL: {}, Response: {}, Website is {}\n".format(datetime.now(),
                                                                        pingList["URL"][value],
                                                                        pingList["Response"][value],
                                                                        pingList["Result"][value]))

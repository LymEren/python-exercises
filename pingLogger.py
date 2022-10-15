# The program pinging in pingHost.txt file

import os
from datetime import datetime

pingList = {
    "URL"      : [],
    "Response" : [],
    "Result"   : []
}

urlCounter = int(input("Kac tane URL pinglemek istiyorsunuz?: "))

for value in range(urlCounter):
    pingInput = input(f"Pinglemek istediginiz {value + 1}. URL'i giriniz: ")
    pingList["URL"].append(pingInput)

for value in range(urlCounter):
    if (os.system("ping " + pingList["URL"][value])) == 0:
        pingList["Response"].append("200")
        pingList["Result"].append("UP")
    else:
        pingList["Response"].append("500")
        pingList["Result"].append("DOWN")

    with open('pingHost.txt', 'a') as pLog:
        pLog.write("{} - URL: {}, Response: {}, Website is {}\n".format(datetime.now(), pingList["URL"][value], pingList["Response"][value], pingList["Result"][value]))


print(pingList)






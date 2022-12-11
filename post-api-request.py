# API POST example
import requests

url = #API Url

# We have made such definitions so that Python can adapt to the json format.
null = None
true = True
false = False

myReq = {#Your Request}

logReq = requests.post(url, json=myReq)
print(logReq.text)
print(logReq.status_code)

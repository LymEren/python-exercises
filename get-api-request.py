#  GET API Request Example

import requests

# CSR Customer Demographic Information API
url = #URL
myReq = requests.get(url, headers={
    'Authorization': 'Bearer #Bearer Key'})


print(myReq.text)
print(type(myReq))

# Here we parse the response.
data = myReq.json()

print(f"\nFirst Key: {data['key']}\nSecond Key: {data['keyTwo']}\nKey Third: {data['keyThird']}")

import requests, json

# local url
url = 'http://127.0.0.1:5000/' # change to your url

# sample data
data = {'Pclass': 3
      , 'Age': 2
      , 'SibSp': 1
      , 'Fare': 50}
data = json.dumps(data)

send_request = requests.post(url, data)
print(send_request.json())

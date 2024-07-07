import requests, json

URL='http://127.0.0.1:8000/stucreate/'
#You called this URL via POST, so it should end with a '/'

data={
    'name':'Rahul',
    'roll':101,
    'city':'Ranchi'
}

#we have to post this data to the above URL
json_data=json.dumps(data)

r=requests.post(url=URL, data=json_data)
#for the res in views.py
try: 
    data=r.json()
    print(data)
except requests.exceptions.JSONDecodeError:
    print("Error: Received response is not a valid JSON")

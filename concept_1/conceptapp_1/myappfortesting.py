import requests

URL="http://127.0.0.1:8000/stuinfo/"

r=requests.get(url=URL)
#here r is the response

data=r.json()

print("Application data from API")
print(data)
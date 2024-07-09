import requests, json

URL="http://127.0.0.1:8000/stu_fns/"

def get_data(id=None):
    #in case the id is None, we get all data from api(queryset) or  we get a particular model object
    data={}
    if id is not None:
        data={'id':id}
    #convert the data(here=id or none) to json
    json_data=json.dumps(data)
    #now send a get request to the url to get data with id=id from url
    r=requests.get(url=URL, data=json_data)
    #A get request is sent, and its response is stored in r

    received_response=r.json()
    print(received_response)

#call functions
# get_data(1)
# get_data()

def post_data():
    data={
        'name': 'Chirag Parakh',
        'roll':25,
        'city':'Jaisalmer'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL, data=json_data)
    received_response=r.json()
    print(received_response)

#call function for testing
# post_data()

def update_data():
    data={
        'id':8,
        'name':'Anand Dugga Rajasthani',
        
    }

    json_data=json.dumps(data)
    r=requests.put(url=URL, data=json_data)
    received_response=r.json()
    print(received_response)

update_data()

def delete_data():
    data={
        'id':4
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL, data=json_data)
    received_response=r.json()
    print(received_response)

#delete_data()





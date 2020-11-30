import requests
import json

def send(index, data,_id):
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data)
    x = requests.put("http://172.31.40.133/"+index+"/_doc/"+_id,headers=headers,data=data)
    print(x.text)

def retrieve_all(index):
    x = requests.get("http://172.31.40.133/"+index+"/_search")
    response = json.loads(x.text)
    hits = response['hits']['hits']
    result = {}
    for y in hits:
        result[y["_id"]] = y["_source"]
    return result
    
def retrieve(index,_id):
    x = requests.get("http://172.31.40.133/"+index+"/_source/"+_id)
    response = json.loads(x.text)
    return(response)
    
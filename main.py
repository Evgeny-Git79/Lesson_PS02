from sqlite3.dbapi2 import paramstyle
import requests
import pprint

#Zadanie1
params ={
    'q': 'language:html'
}
response = requests.get('https://api.github.com/search/repositories', params= params)
print(response.status_code)
print(response.json())
#Zadanie2
params1 ={
    'userId': '1'
}
response1 = requests.get('https://jsonplaceholder.typicode.com/posts', params= params1)
print(response1.status_code)
pprint.pprint(response1.json())

#zadanie3
params3 = {'title': 'foo', 'body': 'bar', 'userId': 1}
response2 = requests.post('https://jsonplaceholder.typicode.com/posts', json=params3)
print(response2.status_code)
pprint.pprint(response2.json())


import requests
from requests import status_codes

#Melakukan input data yang akan dimasukkan pada json
load_data = {"title":"recommendation", "body":"motorcycle", "userId":12}

#Melakukan POST data yang ingin diinput pada link json
r = requests.post("https://jsonplaceholder.typicode.com/posts", json = load_data)

#Mencetak hasil data (response) yang telah diinput
print(r.text)
print("\n")

#Mencetak status request
print("Status:")
print(r.status_code)
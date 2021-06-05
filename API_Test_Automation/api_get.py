import json
from urllib import request

#Menetapkan url json yang akan digunakan
url = "https://jsonplaceholder.typicode.com/posts"

#Melakukan permintaan/penarikan (GET) data pada url
response = request.urlopen(url)

#Membaca data json
data = json.loads(response.read())

#Make sure bahwa seluruh data userId adalah integer
print("Seluruh tipe data pada userId")
for isi_data in range(len(data)):
    print(type(data[isi_data]["userId"]))
    if type(data[isi_data]["userId"]) == int:
        print("True")
    else:
        print("False")
    print("===============")

print("\n")

#Make sure bahwa seluruh data id adalah integer
print("Seluruh tipe data pada id")
for isi_data in range(len(data)):
    print(type(data[isi_data]["id"]))
    if type(data[isi_data]["id"]) == int:
        print("True")
    else:
        print("False")
    print("===============")

print("\n")

#Make sure bahwa seluruh data title adalah string
print("Seluruh tipe data pada title")
for isi_data in range(len(data)):
    print(type(data[isi_data]["title"]))
    if type(data[isi_data]["title"]) == str:
        print("True")
    else:
        print("False")
    print("===============")

print("\n")

#Make sure bahwa seluruh data body adalah string
print("Seluruh tipe data pada body")
for isi_data in range(len(data)):
    print(type(data[isi_data]["body"]))
    if type(data[isi_data]["body"]) == str:
        print("True")
    else:
        print("False")
    print("===============")
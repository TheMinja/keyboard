import requests

char = 'd'

url = 'http://localhost:3000/send/' + str(ord(char))

print(url)

x = requests.post(url)

print(x.text)
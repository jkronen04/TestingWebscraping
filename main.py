import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# requests.get('https://api.github.com')

print(page.text)

response = requests.get('https://realpython.github.io/fake-jobs/')

if response:
    print("Success!")
    print(response.status_code)
elif response.status_code == 404:
    print("Not found.")

    print(response.content)
    #response.headers['viewpoint']

import requests
from bs4 import BeautifulSoup
response = requests.get('https://github.com')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print(soup.prettify())
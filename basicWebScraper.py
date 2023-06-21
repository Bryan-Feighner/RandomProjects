import requests
import bs4 as beautifulSoup
formData = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://oxylabs.io/blog', data = formData)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)
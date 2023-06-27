import bs4
import requests
user = input("Please type in your desired Github User:\n")
repo = input("Please type in your desired repository:\n")
url = 'https://github.com/' + user + '/' + repo
reqResult = requests.get(url)
soup = bs4.BeautifulSoup(reqResult.text, "html.parser")
print(soup.p[''])
import bs4
import requests
text= input("Please type your desired search phrase:\n")
numResults = input("Please type in your desired number of results:\n")
url = 'https://google.com/search?q=' + text + '&num=' + numResults
reqResult = requests.get(url)
soup = bs4.BeautifulSoup(reqResult.text, "html.parser")
headObject = soup.find_all('h3')
links = soup.find_all('a')
for link in links:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
      title = link.find_all('h3')
      if len(title) > 0:
          print(link.get('href').split("?q=")[1].split("&sa=U")[0])
          print(title[0].getText())
          print("")
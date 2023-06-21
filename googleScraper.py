from google_search_scraper_python import *
google.search(keyword="shoes")
for i in range(0,5):
	response=google.search_results()
	data=response["body"]
	print(data)
	google.click_next()

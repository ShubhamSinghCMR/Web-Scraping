import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r=requests.get(url)

if r.status_code != 200:
    print("Unable to access website")

soup = BeautifulSoup(r.text, "lxml")

price = soup.find("h4",{"class":"price float-end card-title pull-right"})
print (price.string)

# Other way to pass attribute
price = soup.find("h4", class_ = "price float-end card-title pull-right")
print (price.string)

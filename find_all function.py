import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r=requests.get(url)

if r.status_code != 200:
    print("Unable to access website")

soup = BeautifulSoup(r.text, "lxml")

prices = soup.find_all("h4", class_ = "price float-end card-title pull-right")

# Display whole list of prices
print(prices)

# Print one by one
for i in prices:
    print(i)
    
# Print Only Price
for i in prices:
    print(i.text)
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

# Checking status
r=requests.get(url)

if r.status_code != 200:
    print("Unable to access website")

# Retrieving XML data 
soup = BeautifulSoup(r.text,"lxml")

# Accessing HTML Tags
print(soup.div)

# Accessing ul tag inside it
print(soup.div.ul)
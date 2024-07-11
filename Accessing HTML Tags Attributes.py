import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r=requests.get(url)

if r.status_code != 200:
    print("Unable to access website")

soup = BeautifulSoup(r.text, "lxml")

# Accessing Header Tag Attributes
tag = soup.header
atb= tag.attrs

print("Attributes: ")
print(atb)

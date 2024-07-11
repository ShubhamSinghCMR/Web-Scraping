import requests, re
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones"

r=requests.get(url)

if r.status_code != 200:
    print("Unable to access website")

soup = BeautifulSoup(r.text, "lxml")

# Finding elements by exact string match
data_exact = soup.find_all(string="Nokia X")
print("Exact match:")
print(data_exact)

# Finding elements by substring match using regular expression
data_regex = soup.find_all(string=re.compile("Nokia"))
print("\nRegex match:")
print(data_regex)
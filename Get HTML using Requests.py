import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

# Using requests library
r= requests.get(url)

if r.status_code != 200:
    print("Unable to access website")

# Check the status
print(f"Website status is {r.status_code}")

# Get HTML of this url
print("The HTML Text is as follows:")
print(r.text)
import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/phones"
r=requests.get(url)

if r.status_code!=200:
    print("Unable to load website")
    exit()

soup = BeautifulSoup(r.text,"lxml")

# Finding product names
name_data = soup.find_all("a", class_ = "title")

product_names = []

for i in name_data:
    product_names.append(i.text)
    
print(f"All products: {product_names}")

# Fiding product prices
price_data = soup.find_all("h4", class_="price float-end card-title pull-right")

prices = []

for i in price_data:
    prices.append(i.text)

print(f"Prices: {prices}")

# Finding product description
description_data = soup.find_all("p", class_="description card-text")

description = []

for i in description_data:
    description.append(i.text)

print(f"Descriptions: {description}")

# Creating a dataframe
df= pd.DataFrame({"product_name": product_names, "Prices": prices, "Description": description})

print(df)

# Exporting to CSV
df.to_csv("product details.csv")
print("Exported to csv..")

# Exporting to Excel
df.to_excel("product details.xlsx")
print("Exported to excel..")

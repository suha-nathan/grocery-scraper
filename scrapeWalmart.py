from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
"""
Categories of interes:

Walmart -> Grocery:
Fruits and vegetables
Dairy and eggs
Meat and seafood

Superstore:
https://api.pcexpress.ca/pcx-bff/api/v1/products/search

Fruits and vegetables
Dairy and eggs
Meat 
Fish and seafood
Frozen Food -> Frozen Fruits and vegetables, Frozen Meat and Seafood

Costco -> Grocery and Household
Meat 
Poultry
Seafood

X fresh vegetables 
X fresh meat/seafood. only prepackaged

"""

# html = urlopen("https://www.walmart.ca/en/browse/grocery/meat-seafood-alternatives/fresh-chicken-turkey/10019_6000194327357_6000194327409?icid=landing/cp_page_grocery_shop_all_chicken_17000_1MS64GM8BT")
# bs = BeautifulSoup(html.read(), "html.parser")

# print(bs)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0)'}
url= "https://www.controlleremea.co.uk/"

html_page = requests.get(url, headers=headers)

bs  = BeautifulSoup (html_page.text, 'html.parser')

print(bs)
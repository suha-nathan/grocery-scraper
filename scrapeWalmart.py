from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

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


html = urlopen("")
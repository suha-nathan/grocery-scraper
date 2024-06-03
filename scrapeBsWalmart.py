import requests 
from bs4 import BeautifulSoup 

walmart_product_url = 'https://www.walmart.com/ip/AT-T-iPhone-14-128GB-Midnight/1756765288' 
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'} 

response = requests.get(walmart_product_url, headers=headers) 
soup = BeautifulSoup(response.content, 'html.parser') 
print(soup.prettify()) 
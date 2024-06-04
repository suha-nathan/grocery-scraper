import requests
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

reqUrl = "https://api.pcexpress.ca/pcx-bff/api/v1/products/search"

headersList = {
 "x-apikey": os.getenv("S_API_KEY"), #api key -> need to generate
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "pagination": {
    "from": 0,
    "size": 48
  },
  "banner": "superstore",
  "cartId": os.getenv("S_CART_ID"), #cart id need to generate
  "lang": "en",
  "date": "03062024", # change this every day
  "storeId": "1077",
  "pcId": "null",
  "pickupType": "STORE",
  "offerType": "ALL",
  "term": "beef",
  "userData": {
    "domainUserId": os.getenv("S_DOMAIN_ID") , # user id-> need to generate
    "sessionId": os.getenv("S_SESSION_ID") # session id-> need to generate
  }
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)


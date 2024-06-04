import requests
import json
import requests
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

def get_cookie():
    with sync_playwright as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.realcanadiansuperstore.ca/")
        cookies = context.cookies()
        browser.close()
    return cookies

def send_request():
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
    "cartId": os.getenv("S_CART_ID"), # lcl-cart-id-banner
    "lang": "en",
    "date": "03062024", # change this every day
    "storeId": "1077",
    "pcId": "null",
    "pickupType": "STORE",
    "offerType": "ALL",
    "term": "beef", #search query
    "userData": {
        "domainUserId": os.getenv("S_DOMAIN_ID") , # sp_domain_userid
        "sessionId": os.getenv("S_SESSION_ID") # sp_domain_sessionid
    }
    })

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(get_cookie())
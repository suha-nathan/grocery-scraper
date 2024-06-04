import requests
import json
import requests
import os
import time
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
        context.close()
        browser.close()
    return cookies

def send_request(cart_id, domain_id, session_id):
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
    "cartId": cart_id, 
    "lang": "en",
    "date": "03062024", # change this every day
    "storeId": "1077",
    "pcId": "null",
    "pickupType": "STORE",
    "offerType": "ALL",
    "term": "beef", #search query
    "userData": {
        "domainUserId": domain_id , 
        "sessionId": session_id
    }
    })

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

# if __name__ == '__main__':
#     cookie = get_cookie()
#     send_request(os.getenv("S_CART_ID"), os.getenv("S_DOMAIN_ID"), os.getenv("S_SESSION_ID"))# lcl-cart-id-banner,# sp_domain_userid, sp_domain_sessionid

print(get_cookie())
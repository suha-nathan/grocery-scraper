import os
import time
import random
import undetected_chromedriver as uc
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
#load variables from .env file
load_dotenv()

driver_path = os.getenv("DRIVER_PATH")

# Setup options to run headless
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options) 
"""
# driver = uc.Chrome()

driver = webdriver.Chrome()
file_path = os.path.abspath("./offline-testing/Online Shopping Canada_ Everyday Low Prices at Walmart.ca!.html")
file_url = f"file:///{file_path}"
# driver.get("https://www.walmart.ca/en")
driver.get(file_url)

time.sleep(6)

try:
    button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Departments']"))) 
    # button = driver.find_element(By.XPATH, "//button[text()='Departments']")
    button.click()
    print("Button clicked successfully")

except Exception as e:
    print(f"an error occured: {e}")
    time.sleep(5)
finally:
    time.sleep(5)
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # ✅ Import Service
import time
from sys import argv as av


url = "https://www.avantorsciences.com/fr/fr/search/"
url += av[1]

# Set up ChromeOptions
options = Options()
options.binary_location = '/home/koyo/chrome-linux64/chrome'  # ✅ Your custom Chrome binary

# Set up ChromeDriver service
service = Service("/home/koyo/chrome/chromedriver")  # ✅ Replace with actual path to chromedriver

# Start the driver with service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to your URL
driver.get(url)
time.sleep(2)

i = driver.find_element(By.CLASS_NAME, "container")
items = i.find_elements(By.CLASS_NAME, "cx-product-container")

for i in items:
    image = i.find_element(By.TAG_NAME, "img").get_attribute("src")
    print(image, end="---\n")
    print(i.text)

driver.quit()

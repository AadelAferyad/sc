

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # ✅ Import Service

url = "https://www.avantorsciences.com/fr/fr/search/"

# Set up ChromeOptions
options = Options()
options.binary_location = '/home/aaferyad/goinfre/chrome-linux64/chrome'  # ✅ Your custom Chrome binary

# Set up ChromeDriver service
service = Service("/path/to/chromedriver")  # ✅ Replace with actual path to chromedriver

# Start the driver with service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to your URL
driver.get(url)

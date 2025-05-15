from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Your search URL
url = "https://www.google.com/search?q=beautifulsoup"

# Setup Firefox options (optional)
options = Options()
options.add_argument('--headless')  # Uncomment this line to run in headless mode

# Path to your geckodriver binary
service = Service("/home/aaferyad/goinfre/geckodriver")  # ✅ Confirm this is correct and executable

# Create the WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Open the URL
driver.get(url)

# Wait to see results (for testing)
time.sleep(10)

# Close the browser
driver.quit()

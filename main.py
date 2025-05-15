from requests import get
from bs4 import BeautifulSoup
from sys import argv as av
from selenium import webdriver


url =  "https://www.avantorsciences.com/fr/fr/search/"
path = '/home/aaferyad/goinfre/chrome-linux64'
driver = webdriver.Chrome(path)
driver.get(url)
# def main(url, headers):
#     length = len(av)
#     # checking if there is enough arguments
#     if (length < 2):
#         print("Error no enough arguments\nUsage: python3 main.py URL keywords")
#         return None
#     # print(url)
#     # appending searching keyword to the url
#     keyword = av[1]
#     url += keyword;
#     # print(url)
#     data = get(url, headers=headers)
#     # print(data.text)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     # print(soup.find_all("div", class_="container"))
#     print(soup.prettify())
#     # class="cx-product-container"
#



# main(url, headers)

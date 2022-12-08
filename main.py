''' Research:
        - for machine learning I will use scikit- learn library/ or the scipy one
        - I will also use the w3 schools resource on machine learning https://www.w3schools.com/python/python_ml_mean_median_mode.asp
        - I will also by using the numpy module to work with numbers
        - importing matplotlib to deal with graphs
        - using selenium to import data from stock website
        # '''


# import selenium
from xpaths import *
import matplotlib.pyplot as plt

# 

# plt.scatter(x, y)
# plt.show()
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By




from selenium.webdriver.common.action_chains import ActionChains

#asks the user for imput and and then launches a chrome window where it navigates to the 
#yahoo finance page for that symbol
symbol = input("enter the stock symbol")
browser = webdriver.Chrome()
action = ActionChains(browser)

browser.implicitly_wait(0.5)
browser.get ("https://finance.yahoo.com/quote/" + symbol)

browser.implicitly_wait(11)
# alert = Alert(browser)
# alert.dismiss
# alert = browser.switch_to.alert
# alert.dismiss
later = browser.find_element(By.XPATH, "//*[@id=\"myLightboxContainer\"]/section/button[2]")
print (later.text)

later.click()

historical = browser.find_element(By.XPATH, "//*[@id=\"quote-nav\"]/ul/li[6]/a")
print (historical.text)




historical.click ()


x = 1
price_results = browser.find_elements (By.XPATH,"//*[@id=\"Col1-1-HistoricalDataTable-Proxy\"]/section/div[2]/table/thead/tr/th[5]")
browser.implicitly_wait(5)
price1found = []

def price_scrape ():
    x = 1
    while x !=15:
       priceElements = browser.find_elements (By.XPATH, "//*[@id=\"Col1-1-HistoricalDataTable-Proxy\"]/section/div[2]/table/tbody/tr[" + str(x) + "]/td[5]/span")
       if priceElements.count() == 1:
         print(priceElements[0].text)
         price1found.append(priceElements[0].text)
       x += 1



#//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]/span
# browser.find_element(By.XPATH ("// a[contains(text(),\'Maybe Later')]")).click()
# date_results = browser.find_elements(By.XPATH,browser.find_elements(By.ID,"Col1-1-HistoricalDataTable-Proxy"))
# pri = browser.find_elements(By.XPATH,"//span[contains(@class,'ng-binding')]")

# datefound = []
# for i in date_results:
#     if len(i.text) > 0:
#         datefound.append(i.text)
#     if len(datefound) > 45:
#         break

price_scrape()
print (price1found)
browser.implicitly_wait(0.5)
time.sleep(3)

# plt.scatter(datefound, price1found)
# plt.show()#so the user can actually see something

#https://www.tutorialspoint.com/google-search-automation-with-python-selenium

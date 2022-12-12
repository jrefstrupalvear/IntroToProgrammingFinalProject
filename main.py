''' 
Joshua Refstrup Alvear
Research:
        - for machine learning I will use scikit- learn library/ or the scipy one
        - I will also use the w3 schools resource on machine learning https://www.w3schools.com/python/python_ml_mean_median_mode.asp
        - I will also by using the numpy module to work with numbers
        - importing matplotlib to deal with graphs
        - using selenium to import data from stock website
        # '''

#https://www.tutorialspoint.com/google-search-automation-with-python-selenium
#selenium documentation
#dad's help
#prices are closing prices
# import selenium
# https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/
  #above website of explicit wait
from xpaths_and_settings import *
import matplotlib.pyplot as plt
from selenium.webdriver.support.ui import WebDriverWait
import time
import scipy as sp
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np

from selenium.webdriver.support import expected_conditions as EC



from selenium.webdriver.common.action_chains import ActionChains

#asks the user for imput and and then launches a chrome window where it navigates to the 
#yahoo finance page for that symbol
symbol = input("enter the stock symbol")
browser = webdriver.Chrome()

browser.implicitly_wait(0.5)
browser.get ("https://finance.yahoo.com/quote/" + symbol)






Element = WebDriverWait(browser, 20).until(
       EC.presence_of_element_located((By.XPATH, "//*[@id=\"myLightboxContainer\"]/section/button[2]"))
)
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
    while x !=16:
       priceElements = browser.find_elements (By.XPATH, "//*[@id=\"Col1-1-HistoricalDataTable-Proxy\"]/section/div[2]/table/tbody/tr[" + str(x) + "]/td[5]/span")
       if len(priceElements) == 1:
         price1found.append(float(priceElements[0].text))
       x += 1







price_scrape()
price1found = np.array(price1found)
print (price1found)
print(numbers)

browser.implicitly_wait(0.5)
time.sleep(3)

plt.scatter(numbers, price1found)
plt.show()#so the user can actually see something


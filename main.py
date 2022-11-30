''' Research:
        - for machine learning I will use scikit- learn library/ or the scipy one
        - I will also use the w3 schools resource on machine learning https://www.w3schools.com/python/python_ml_mean_median_mode.asp
        - I will also by using the numpy module to work with numbers
        - importing matplotlib to deal with graphs
        - using selenium to import data from stock website
        - will use beautiful soup to scrape the data'''
        # 


# import selenium
# import matplotlib.pyplot as plt

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(x, y)
# plt.show()
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#asks the user for imput and and then launches a chrome window where it navigates to the 
#yahoo finance page for that symbol
symbol = input("enter the stock symbol")
browser = webdriver.Chrome()
browser.implicitly_wait(0.5)
browser.get ("https://finance.yahoo.com/quote/" + symbol)
# alert = browser.switch_to.alert
# alert.dismiss

#so the user can actually see something
browser.implicitly_wait(0.5)
time.sleep(3)

#https://www.tutorialspoint.com/google-search-automation-with-python-selenium

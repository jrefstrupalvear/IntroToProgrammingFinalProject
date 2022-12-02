# plt.scatter(x, y)
# plt.show()
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert



#asks the user for imput and and then launches a chrome window where it navigates to the 
#yahoo finance page for that symbol
symbol = input("enter the stock symbol")
browser = webdriver.Chrome()
browser.implicitly_wait(0.5)
browser.get ("https://google.com")

browser.implicitly_wait(11)

close = browser.find_element(By.XPATH, "//*[@id='gbqfbb']")
close.click


time.sleep (5)
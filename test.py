# 

# plt.scatter(x, y)
# plt.show()
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert



from selenium.webdriver.common.action_chains import ActionChains

#asks the user for imput and and then launches a chrome window where it navigates to the 
#yahoo finance page for that symbol
symbol = input("enter the stock symbol")
browser = webdriver.Chrome()
action = ActionChains(browser)

browser.implicitly_wait(0.5)
browser.get ("https://finance.yahoo.com/quote/" + symbol)

browser.implicitly_wait(4)
# alert = Alert(browser)
# alert.dismiss
# alert = browser.switch_to.alert
# alert.dismiss
later = browser.find_element(By.XPATH, "//*[@id=\"myLightboxContainer\"]/section/button[2]")
print (later.text)

later.click

browser.implicitly_wait(5)
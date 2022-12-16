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
from scipy import stats
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np

from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.action_chains import ActionChains
price1found = []
price2found = []
price3found = []
price4found = []

class Scraper:
  def __init__(self, pri1, pri2,arr):
    x = 1
    
    self.pri1 = pri1
    self.pri2 = pri2
    self.arr = arr

    while x !=16:
       priceElements = browser.find_elements (By.XPATH, pri1+str(x)+pri2)
       if len(priceElements) == 1:
         arr.append(float(priceElements[0].text))
       x += 1
#asks the user for imput and and then launches a chrome window where it navigates to the 
#yahoo finance page for that symbol
symbol = input("enter the stock symbol")
browser = webdriver.Chrome()
# waits for the window to pop up
browser.implicitly_wait(0.5)
#takes us to the website we want to go -- works together with user input
browser.get ("https://finance.yahoo.com/quote/" + symbol)






#waits until an element is located, it will wait for a maximum of 20 seconds
# the element in our case is the maybe later popup we need to click
Element = WebDriverWait(browser, 25).until(
       EC.presence_of_element_located((By.XPATH, "//*[@id=\"myLightboxContainer\"]/section/button[2]"))
)

#finds that same element
later = browser.find_element(By.XPATH, "//*[@id=\"myLightboxContainer\"]/section/button[2]")
print (later.text)

# clicks that element
later.click()


#finds the historical data tab from which the data will be pulled
historical = browser.find_element(By.XPATH, "//*[@id=\"quote-nav\"]/ul/li[6]/a")
print (historical.text)

#clicks the historical data tab
historical.click ()


# waits for the browser to actually load the historical data
browser.implicitly_wait(5)

#instantiating the classes 
closing_price = Scraper (price1,price2,price1found) 
closing_price
opening_price = Scraper (price1_2, price2_2,price2found)
high_price = Scraper (price1_3,price2_3, price3found)
low_price = Scraper(price1_4,price2_4,price4found)

# the arrays created in the class must be converted into a numpy array
# doing this for all of them.... 

price1found = np.array(price1found)
price2found = np.array(price2found)
price3found = np.array(price3found)
price4found = np.array(price4found)


# getting the slope for all of the lines with linear regression so that it will make a loose prediction
# of where the stocks will actually go
slope, intercept, r, p, std_err = stats.linregress (numbers, price1found)
slope, intercept, r, p, std_err = stats.linregress (numbers, price2found)
slope, intercept, r, p, std_err = stats.linregress (numbers, price3found)
slope, intercept, r, p, std_err = stats.linregress (numbers, price4found)



def prediction (x):
  return slope * x +intercept



mypredic1 = list(map(prediction,numbers))
mypredic2 = list(map(prediction,numbers))

print (price1found)
print(numbers)

browser.implicitly_wait(0.5)
time.sleep(3)
plt.subplot(1,2,1)
plt.scatter(numbers, price1found)
plt.title("Closing Prices")
plt.plot (numbers, mypredic1)
plt.subplot(1,2,2)
plt.scatter(numbers, price2found)
plt.title("Opening Prices")
plt.plot (numbers,mypredic2)
plt.show()#so the user can actually see something


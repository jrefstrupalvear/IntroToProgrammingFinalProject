''' 
Joshua Refstrup Alvear
Research:
        - for machine learning I will use scikit- learn library/ or the scipy one
        - I will also use the w3 schools resource on machine learning https://www.w3schools.com/python/python_ml_mean_median_mode.asp
        - I will also by using the numpy module to work with numbers
        - importing matplotlib to deal with graphs
         - will use scipy for linear regression prediction
        - using selenium to import data from stock website
        # '''
#https://www.w3schools.com/python/default.asp
# #selenium documentation
#https://selenium-python.readthedocs.io/
#Google Search Automation https://www.tutorialspoint.com/google-search-automation-with-python-selenium
#Explicit Wait Tutorial https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/
#Dad's help with XPATHS
#labeling axes https://www.edureka.co/community/102186/how-set-the-figure-title-and-axes-labels-font-size-matplotlib

#imports my settings
from xpaths_and_settings import *
#for graphs
import matplotlib.pyplot as plt
#for chrome navigation and web scraping
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# for waiting
import time
# for linear regression
from scipy import stats
#for dealing with numbers and plotting them (working with matplotlib)
import numpy as np



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
# gets data for the last 25 days
    while x !=27:
      # finds the element using the xpath, the pri1 pri2 seperation is so that I can fit a
      # variable into the equation
       priceElements = browser.find_elements (By.XPATH, pri1+str(x)+pri2)
       #checks to make sure there is something in the priceElements
       if len(priceElements) == 1:
        # appends that to the corresponding list that we put into the parameters as an argument

         arr.append(float(priceElements[0].text))
         #adds one everytime so that it will keep moving down the xpath
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
#I am mainly looking fo the slope
# this is from w3 schools section on linear regression
slope1, intercept, r, p, std_err = stats.linregress (numbers, price1found)
slope2, intercept, r, p, std_err = stats.linregress (numbers, price2found)
slope3, intercept, r, p, std_err = stats.linregress (numbers, price3found)
slope4, intercept, r, p, std_err = stats.linregress (numbers, price4found)


# finding the line for each of the four graphs, 

def prediction1 (x):
  return slope1* x +intercept

def prediction2 (x):
  return slope2* x +intercept

def prediction3 (x):
  return slope3* x +intercept

def prediction4 (x):
  return slope4* x +intercept


# makes the data from the functions into a list
mypredic1 = list(map(prediction1,numbers2))
mypredic2 = list(map(prediction2,numbers2))
mypredic3 = list(map(prediction3,numbers2))
mypredic4 = list(map(prediction4,numbers2))

print (price1found)
print(numbers)

browser.implicitly_wait(0.5)
time.sleep(3)

# setting the figure size so that it takes up most of the screen
plt.figure(figsize=(20,10))

#subplots are so that we can see all the data on one screen on multiple graphs, not just on one graph 
#the arguments are (number of rows, number of columns, position)
plt.subplot(2,2,1)
#plots the scatter plot using numbers as the x and the price1found array on the y axis
plt.scatter(numbers, price1found)
#naming the individual graphs so the user can differenciate
plt.title("Closing Prices")
#labeling the axes 
plt.ylabel("Price in $",fontsize=6)
plt.xlabel ("Days (today is 0)",fontsize=6)
# ploting the line we found using linear regression
plt.plot (numbers2, mypredic1)

# doing all of this with the other graphs

plt.subplot(2,2,2)
plt.scatter(numbers, price2found)
plt.title("Opening Prices")
plt.ylabel("Price in $",fontsize=6)
plt.xlabel ("Days (today is 0)",fontsize=6)
plt.plot (numbers2,mypredic2)

plt.subplot(2,2,3)
plt.scatter(numbers,price3found)
plt.title ("High Prices")
plt.ylabel("Price in $",fontsize=6)
plt.xlabel ("Days (today is 0)",fontsize=6)
plt.plot(numbers2,mypredic3)

plt.subplot(2,2,4)
plt.scatter(numbers,price4found)
plt.title ("Low Prices")
plt.ylabel("Price in $",fontsize=6)
plt.xlabel ("Days (today is 0)",fontsize=6)
plt.plot(numbers2,mypredic4)


#so the user can actually see something
plt.show()


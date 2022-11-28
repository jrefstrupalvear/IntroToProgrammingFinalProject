''' Research:
        - for machine learning I will use scikit- learn library/ or the scipy one
        - I will also use the w3 schools resource on machine learning https://www.w3schools.com/python/python_ml_mean_median_mode.asp
        - I will also by using the numpy module to work with numbers
        - importing matplotlib to deal with graphs
        - using selenium to import data from stock website'''


# import selenium
# import matplotlib.pyplot as plt

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.scatter(x, y)
# plt.show()


#progress of 11/28/2022 - research and working on navigating webpages with python, still don' understand the code, I am trying to learn it
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
stock_symbol = input("Please Enter the Stock Symbol You Want to Analyze")
driver = webdriver.Chrome('./chromedriver')
driver.get("https://finance.yahoo.com/")
print(driver.title)
search_bar = driver.find_element("name", "q")
search_bar.clear()
search_bar.send_keys(stock_symbol)
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()

time.sleep(5) # Let the user actually see something!

driver.quit()

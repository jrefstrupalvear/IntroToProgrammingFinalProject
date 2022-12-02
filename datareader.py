# sources: https://www.geeksforgeeks.org/writing-excel-sheet-using-python/


############## open website with selenium and webdriver ###################
from time import sleep
import xlwt
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# scrape page
URL = 'https://www.pro-football-reference.com/years/2022/rushing.htm'
# URL = 'https://herenow.com/results/#/races/20899/results'

chrome_driver = "Code\Projects\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get(URL)
sleep(5)
# spans = driver.find_element(By.TAG_NAME, "span")
# print(type(spans))


#################### write to excel #########################

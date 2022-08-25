from selenium import webdriver
import time
browser = webdriver.Chrome()


browser.get("https://www.google.com")

# Im feeling lucky page
lucky_page = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]")  

time.sleep(5)

lucky_page.click()

time.sleep(5)

browser.close()




################## 2 


from lib2to3.pgen2 import driver

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

firstDriver = webdriver.Chrome()

firstDriver.get("https://www.google.com")

firstDriver.maximize_window()
sleep(1)

searchBox = firstDriver.find_element(By.NAME,"q")
searchBox.send_keys("kodlama.io")
sleep(2)

searchBox.send_keys('\ue007') # searchBox.send_keys(Keys.ENTER)

sleep(2)

firstResult = firstDriver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")

print(firstResult.get_attribute("href")) == ("https://www.kodlama.io")

# firstResult.click()




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

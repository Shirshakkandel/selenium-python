import selenium
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://shirshakkandel.com.np")
print(driver.title)
driver.quit()

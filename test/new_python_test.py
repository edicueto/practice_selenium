from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Users\Edessa\Documents\practice_selenium\drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit()

# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

for link in driver.find_elements_by_xpath("//*[@id='u1']/a"):
    print(link.get_attribute('href'))
    #查看页面所有元素具有id值
    print(link.get_attribute('id'))
driver.quit()


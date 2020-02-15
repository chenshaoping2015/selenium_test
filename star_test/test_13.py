# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
import win32api

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

element = driver.find_element_by_xpath("//*[@id='lg']/img[1]")
actionChains = ActionChains(driver)
actionChains.context_click(element).perform()
# actionChains.context_click(element).send_keys('i').perform()
time.sleep(1)
win32api.keybd_event(73,0,0,0)


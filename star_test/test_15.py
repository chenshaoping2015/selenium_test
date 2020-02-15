import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("file:///C:/Users/stevechen/Desktop/testhtml/test_ifram.html")
time.sleep(1)

driver.switch_to.frame("frame1")
driver.find_element_by_id('kw').send_keys("selenium")#搜索框输入selenium
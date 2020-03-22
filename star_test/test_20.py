# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

driver.find_element_by_link_text("登录").click()
time.sleep(8)
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
time.sleep(2)
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("you14563@163.com")
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("2010080101303")
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
time.sleep(3)
dictCookies = driver.get_cookies()
print(dictCookies)
driver.switch_to.alert

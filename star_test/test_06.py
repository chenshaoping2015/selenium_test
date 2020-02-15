#coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://www.baidu.com')
try:
    driver.find_element_by_class_name('s_ipt')
    print('test pass:element found by class name')
except Exception as e:
    print("Exception found",format(e))

driver.quit()


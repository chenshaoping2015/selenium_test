#coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://www.baidu.com')
try:
    driver.find_element_by_link_text('新闻')
    print('test pass:element found by link text')
except Exception as e:
    print("Exception found",format(e))

driver.quit()
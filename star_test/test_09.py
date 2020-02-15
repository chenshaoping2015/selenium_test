#coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://wenku.baidu.com/')
driver.implicitly_wait(2)

for i in driver.find_elements_by_name('lm'):
    print(i)
    i.click()
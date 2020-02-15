#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.cnblogs.com/')
driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="span_userinfo"]/a[1]').click()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='submitBtn']/span[1]").click()
time.sleep(2)
# 断言方法，本文重点介绍方法
error_mes = driver.find_element_by_id('LoginName-error').text
print(error_mes)
try:
    assert error_mes == '请输入登录用户名'
    print('Test pass.')
except Exception as e:
    print("Test fail.", format(e))
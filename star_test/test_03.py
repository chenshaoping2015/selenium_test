#coding:utf-8

from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://home.baidu.com/home/index/contact_us")

#得到网页源代码
doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+',doc)# 利用正则，找出 xxx@xxx.xxx 的字段，保存到emails列表
email_value = []
#循环打印邮箱
for email in emails:
    email_value.append(email)
print(email_value)
driver.quit()
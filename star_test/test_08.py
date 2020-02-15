#coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()#打开chrome浏览器
driver.maximize_window()#最大化浏览器窗口
driver.implicitly_wait(3)#设置隐式等待时间

driver.get("https://www.baidu.com")#打开百度
#driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")#搜索框输入selenium
#driver.find_element_by_xpath("//*[@id='su']").click() 点击“百度一下”按钮
time.sleep(2)#等待2秒钟
ele_news = driver.find_element_by_link_text("新闻")
ele_news.click()

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(2)
driver.quit()
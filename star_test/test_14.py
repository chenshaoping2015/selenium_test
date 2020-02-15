# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://tieba.baidu.com/index.html")
time.sleep(1)

target_elem = driver.find_element_by_link_text("地区")
driver.execute_script("return arguments[0].scrollIntoView();", target_elem)  # 用目标元素参考去拖动

time.sleep(4)
driver.execute_script("window.alert('这是一个alert弹框。');")  # 注意这里的分号是英文输入法的分号，不能用中文

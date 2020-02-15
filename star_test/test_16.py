# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

driver.execute_script("window.alert('这是一个测试Alert弹窗');")
print(driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.accept()  # 点击弹出里面的确定按钮
# driver.switch_to_alert().dismiss() # 点击弹出上面的X按钮
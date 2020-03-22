import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()#打开chrome浏览器
driver.maximize_window()#最大化浏览器窗口
driver.implicitly_wait(8)#设置隐式等待时间

driver.get("https://www.baidu.com")#打开百度
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")#搜索框输入selenium
driver.find_element_by_xpath("//*[@id='su']").click()#点击“百度一下”按钮

time.sleep(2)#等待2秒钟

#最多等待3秒直到浏览器标题栏中出现selenium字样
try:
    WebDriverWait(driver,3).until(
        EC.title_contains('selenium')
    )
    print(driver.title)
finally:
    driver.quit()

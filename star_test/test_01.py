from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#初始化一个浏览器实例：driver
driver = webdriver.Chrome()
#最大化浏览器
driver.maximize_window()
#设置隐式时间等待
driver.implicitly_wait(2)
#通过get打开一个页面
driver.get("https://www.baidu.com")

time.sleep(2)
#用find_element_bu_link_text()方法定位
# driver.find_element_by_link_text('新闻').click()
# time.sleep(3)
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'t')

#在新的tab页打开链接的方法
href = driver.find_element_by_link_text("学术").get_attribute('href')#获取百度主页学术的链接
js = "window.open('{}');".format(href)#javaScript语句,通过这条语句在新的标签页打开百度学术
driver.execute_script(js)#执行JavaScript语句

#baidu_handle = driver.current_window_handle# #获取百度主页的窗口句柄

#切换句柄的方法
handles = driver.window_handles#获取浏览器打开的所有标签页的句柄
print('当前句柄：',handles)
driver.switch_to.window(handles[-1])

time.sleep(2)

# try:
#     WebDriverWait(driver,3).until(
#         EC.title_contains('学术')
#     )
#     print(driver.title)
#     print(driver.current_url)
# finally:
#     driver.quit()

# for handle in handles:
#     if handle != baidu_handle:
#         xueshu_handle = handle
# print(baidu_handle,xueshu_handle)
# print('now window handle:',driver.current_window_handle)
# driver.switch_to.window(xueshu_handle)#切换标签页,原本在百度主页的页面,现在切换到百度学术
# print('now window handle:',driver.current_window_handle)

print(driver.current_url)
title = driver.title
print(title)
try :
    assert title in '百度学术 - 保持学习的态度'# 判断页面B标题是否包含页面A标题
    print ('Test Pass.')
except Exception as e:
    print ('Test Fail')
#print(driver.capabilities['version'])
#关闭浏览器
driver.quit()
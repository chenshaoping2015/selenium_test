#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/stevechen/Desktop/testhtml/test_select.html')
driver.implicitly_wait(2)

select = Select(driver.find_element_by_id('choose_car'))
#查看select中所有的选项   select.options
for one in select.options:
    print(one.text)
time.sleep(2)
# 反选所有选中的元素
# select.deselect_all()
# time.sleep(2)

#查看我已选中的选项   all_selected_options
for one in select.all_selected_options:
    print(one.text)

select.select_by_index(1)
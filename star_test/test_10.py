#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/stevechen/Desktop/testhtml/test_checkbox.html')
driver.implicitly_wait(2)

# checkbox
driver.find_element_by_xpath('//input[@value="cv1"]').click()  # click
driver.find_element_by_xpath('//input[@value="cv2"]').send_keys(Keys.SPACE)  # send space
if driver.find_element_by_xpath('//input[@value="cv2"]').is_selected():
    print ('selected!')
else:
    print ('not yet!')
time.sleep(3)

#取消选中所有的复选框；再选择想要选择的复选框
# 根据input属性选中，并且被checked中的元素
checkEles = driver.find_elements_by_css_selector("input[name='subject[0]'][checked]")
for one in checkEles:
    one.click()  # 点击反选

# 再选择点击目标元素
driver.find_element_by_css_selectot("input[value='F1']").click()
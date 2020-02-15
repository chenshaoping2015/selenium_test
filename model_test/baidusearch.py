#coding:utf-8
import time
from selenium import webdriver
from framework.basepage import BasePage

class BaiduSearch():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)

    def test_search(self):
        text = self.driver.find_element_by_id('kw')
        text.send_keys('selenium')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        print(self.driver.title)
        time.sleep(4)
        self.basepage.back()
        time.sleep(2)
        self.basepage.forward()
        # try:
        #     assert 'selenium' in self.driver.title
        #     print("test pass.")
        # except Exception as e:
        #     print("test fail.")
        self.basepage.quit_browser()

if __name__  == '__main__':
    baidusearch = BaiduSearch()
    baidusearch.open_baidu()
    baidusearch.test_search()

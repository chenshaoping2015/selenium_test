# coding=utf-8
import time
from selenium import webdriver
from framework.basepage import BasePage

class TestScreenShot():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1)
    basepage = BasePage(driver)

    def test_take_screen(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)
        self.basepage.take_screenshot()
        self.basepage.quit_browser()

if __name__=='__main__':
    test = TestScreenShot()
    test.test_take_screen()
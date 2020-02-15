#encoding:utf-8
import time
import unittest
from framework.browser_engine import BrowerEngine

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        '''
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        '''
        browser = BrowerEngine()
        self.driver = browser.open_browser()

    def tearDown(self):
        '''
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        '''
        self.driver.quit()

    def test_baidu_search(self):
        '''
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        :return:
        '''
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        try:
            assert 'selenium' in self.driver.title
            print('Test pass')
        except Exception as e:
            print('Test Fail.',format(e))

if __name__=='__main__':
    unittest.main()
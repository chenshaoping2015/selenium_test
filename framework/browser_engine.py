#coding:utf-8
import configparser
from selenium import webdriver
import os.path
from framework.logger import Logger
import time

logger = Logger(logger='BrowserEngine').getlog()

class BrowerEngine():
    '''
    定义一个浏览器引擎类，根据browser_type的值去控制启动不同的浏览器，这里主要是IE，Firefox，Chrome
    '''
    def __init__(self,driver=None):
        #self.browser_type = browser_type
        self.driver = driver


    def open_browser(self):
        config = configparser.ConfigParser()
        file_path = os.path.abspath(os.path.dirname(os.getcwd()))+'/config/config.ini'
        config.read(file_path)

        browser = config.get('browserType','browserName')
        logger.info('You had select %s browser.'% browser)
        url = config.get('testServer','URL')
        logger.info('The test server url is :%s'%url)

#        通过if语句来控制初始化不同浏览器的启动
        try:
            if browser == 'Firefox':
                self.driver = webdriver.Firefox()
                logger.info('Starting Firefox browser.')
            elif browser == 'Chrome':
                self.driver = webdriver.Chrome()
                logger.info('Starting Chrome browser.')
            elif browser == 'IE':
                self.driver = webdriver.Ie()
                logger.info('Starting IE browser.')
        except Exception as e:
            print('open browser error:%s'%e)

        self.driver.get(url)
        logger.info('Open url:%s'%url)
        time.sleep(2)
        self.driver.maximize_window()
        logger.info('Maximize the current window.')
        self.driver.implicitly_wait(2)
        logger.info('Set implicitly wait 6 seconds.')

        return self.driver

    def quit_browser(self):
        logger.info('Now,close and quit the browser.')
        self.driver.quit()

if __name__=='__main__':
     start = BrowerEngine()
     print(dir)
     start.open_browser()
     start.quit_browser()


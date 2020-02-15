#coding:utf-8
import time
import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportsNewsHomePage

class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browser = BrowerEngine()
        self.driver = browser.open_browser()

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_news(self):
        #初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        #baiduhome.click_news()
        self.driver.find_element_by_link_text("新闻").click()
        time.sleep(2)

        #初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.driver)
        #newshome.click_sports()
        self.driver.find_element_by_link_text("体育").click()
        time.sleep(2)

        #初始化一个体育新闻主页，点击NBA
        sportnewhome = SportsNewsHomePage(self.driver)
        #sportnewhome.click_nba_link()
        self.driver.find_element_by_link_text("体育视频").click()
        time.sleep(2)
        sportnewhome.take_screenshot()

if __name__=='__main__':
    unittest.main()

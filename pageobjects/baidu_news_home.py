# coding=utf-8
from framework.basepage import BasePage

class NewsHomePage(BasePage):
    #点击体育新闻入口
    sports_link = "l=>体育"

    def click_sports(self):
        self.click(self.sports_link)
        self.sleep(2)
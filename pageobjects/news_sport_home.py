# coding=utf-8
from framework.basepage import BasePage

class SportsNewsHomePage(BasePage):
    #体育视频入口
    nba_link = "l=>体育视频"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)
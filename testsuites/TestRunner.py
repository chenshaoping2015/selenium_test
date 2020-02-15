#coding:utf-8
import unittest
import os
from testsuites.test_baiduhomepage import BaiduSearch
from testsuites.test_get_page_title import GetPageTitle
from testsuites.test_nba_news_views import ViewNBANews
from base_file import HTMLTestRunner
import time

suite = unittest.TestSuite()
#suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(GetPageTitle('test_get_title'))
#suite.addTest(ViewNBANews('test_view_nba_news'))

if __name__=='__main__':
    # 设置报告文件保存路径
     report_path = os.path.abspath(os.path.dirname(os.getcwd())) + '/test_reports/'
    # print(report_path)
    # 获取系统时间
     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    # 设置报告名称格式
     HtmlFile = report_path+now+"HTMLtemplate.html"
     fp = open('HtmlFile', 'wb')
     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is the first report')
     runner.run(suite)
     fp.close()


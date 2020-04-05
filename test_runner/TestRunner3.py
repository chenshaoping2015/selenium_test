#coding=utf-8
import unittest
import os
import time
from base_file import HTMLTestRunner
from testsuites.test_baiduhomepage import BaiduSearch

#设置路径
report_path = os.path.abspath(os.path.dirname(os.getcwd()))+'/test_reports/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile,"wb")

# 构建suite
suite = unittest.TestLoader().discover("testsuites")

if __name__=='__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="first test report", description="test case results")
    #runner = unittest.TextTestRunner()
    runner.run(suite)


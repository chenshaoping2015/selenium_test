#coding:utf-8

import configparser
import os

class TestReadConfigFile():
    def get_value(self):
        root_dir = os.path.abspath(os.path.dirname(','))# 获取项目根目录的相对路径
        print(root_dir)

        config = configparser.ConfigParser()
        filepath = root_dir+'/config/config.ini'
        config.read(filepath)

        browser = config.get('browserType','browserName')
        url = config.get('testServer','URL')

        return (browser,url)# 返回的是一个元组

trcf = TestReadConfigFile()
print(trcf.get_value())
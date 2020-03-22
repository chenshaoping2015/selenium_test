# coding=utf-8
import time
from selenium import webdriver


class GetSubString(object):

    def get_search_result(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(8)

        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        driver.find_element_by_id('su').click()
        time.sleep(2)
        search_result_string = driver.find_element_by_xpath("//*/span[@class='nums_text']").text
        print(search_result_string)

        new_string = search_result_string.split('约')[1]  # 第一次切割得到 xxxx个，[1]代表切割右边部分
        print(new_string)
        last_result = new_string.split('个')[0]  # 第二次切割，得到我们想要的数字 [0]代表切割参照参数的左边部分
        print(last_result)

if __name__=='__main__':
    getstring = GetSubString()
    getstring.get_search_result()
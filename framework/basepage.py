# coding=utf-8
import os
import time
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException

logger = Logger(logger='BasePage').getlog()

class BasePage(object):
    """
    主要是把常用的几个Selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    back()
    forward()
    get()
    quit()
    """

    def __init__(self, driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()
        logger.info('click back on current page')

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()
        logger.info('click forward on current page')

    # 隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('wait for %s seconds.'% seconds)

    #点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info('closing and quit the browser')
        except NameError as e:
            logger.error('Fail to quit the browser with %s'%e)


    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()

    def take_screenshot(self):
        '''
        截图并保存在根目录下的Screenshots文件夹下
        :return:
        '''
        root_dir = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        file_path = root_dir+'/Screenshots/'
        print(file_path)
        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("开始截图并保存")
        except Exception as e:
            logger.error("出现异常",format(e))

    #定位元素的方法
    def find_element(self,selector):
        '''
        这个地方为什么是根据=>来切割字符串，请看页面定位元素的方法
        submit_btn='id=>su'
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        '''
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element successful "
                            "by %s via value: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.take_screenshot()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                logger.info("Had find the element successful "
                            "by %s via value: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element successful "
                            "by %s via value: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.take_screenshot()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()


    #清除文本框
    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info('Clear text in input box before typing.')
        except NameError as e:
            logger.info('Failed to clear in input box with %s'%e)
            self.take_screenshot()

        # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

        # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

# if __name__=='__main__':
#      driver = webdriver.Chrome()
#      url = 'https://www.baidu.com'
#      input_box = "id=>kw"
#      search_submit_btn = "xpath=>//*[@id='su']"
#
#      homepage = BasePage(driver)
#      homepage.open_url(url)
#      #text = homepage.find_element(input_box)
#      homepage.type(input_box,'selenium')
#      time.sleep(2)
#      btn = homepage.find_element(search_submit_btn)
#      btn.click()
#      time.sleep(4)
#      homepage.quit_browser()



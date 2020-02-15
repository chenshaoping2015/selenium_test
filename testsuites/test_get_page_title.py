import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.baidu_homepage import HomePage

class GetPageTitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowerEngine()
        cls.driver = browser.open_browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        homepage = HomePage(self.driver)
        print(homepage.get_page_title())
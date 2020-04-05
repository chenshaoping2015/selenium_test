import unittest
import testsuites
from testsuites.test_baiduhomepage import BaiduSearch
from testsuites.test_nba_news_views import ViewNBANews
from testsuites.test_get_page_title import GetPageTitle

suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))

if __name__=='__main__':
    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)

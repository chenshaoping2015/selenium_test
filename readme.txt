声明：代码内容来自https://blog.csdn.net/u011541946/category_6788788_2.html
模块划分
|--config 存放配置文件config.ini
|--Log  存放log文件
|--Screenshots  存放截图
|--test_reports 存放测试报告
|--framework
    |--basepage.py  主要是把常用的几个Selenium方法封装到BasePage这个类
    |--browser_engine.py  定义一个浏览器引擎类，根据browser_type的值去控制启动不同的浏览器
    |--logger.py  制定保存日志的文件路径，日志级别，以及调用文件，将日志存在制定的文件中
|--pageobjects
    |--baidu_homepage.py  定义百度新闻入口
    |--baidu_news_home.py   定义百度体育入口
    |--news_sport_hoem.py  定义体育视频入口
|--testsuites
    |--test_baiduhomepage.py    百度关键字搜索测试用例
    |--test_get_page_title.py   获取页面头部信息测试用例
    |--test_nba_news_views.py   百度首页->点击新闻链接->点击视频链接 测试用例
    |--testbaidu.py  百度关键字搜索测试用例
    |--TestRunner.py    unittest之addTest
    |--TestRunner2.py   unittest之makeSuite
    |--TestRunner3.py   unittest之discover
|--model_test
    |--test_config.py   config的测试用例
    |--baidusearch.py   封装百度搜索的步骤
    |--getsubstring.py  python字符串切割
---------------------------------------------------------------------------
类说明
1.BasePage（路径：framework->basepage.py)
定义了12个常用类，调用需输入driver变量

2.BrowserEngine（路径：framework->browser_engine.py)
定义了启动和关闭浏览器两个类，读取本地配置文件获取浏览器和URL

3.Logger（路径：framework->logger.py)
制定保存日志的文件路径，日志级别，以及调用文件，将日志存在制定的文件中,调用先实例化logger = Logger(logger='BasePage').getlog()

----------------------------------------------------------------------------

model_test模块

test_config
    (1)先创建一个config.ini文件;
    (2)创建类TestReadConfigFile读取配置文件内容;
    (3)获取当前项目根目录相对路径：os.path.abspath(os.path.dirname(','));




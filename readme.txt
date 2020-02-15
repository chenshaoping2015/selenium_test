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
|--log_test
    |--get_time 获取系统时间，设置时间格式
    |--log_test.py  log教程
    |--test_logging.py  logger.py的测试用例
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
star_test模块
test_01:
    (1)用js在新的tab页打开链接的方法;
    (2)切换句柄的方法;
    (3)断言;
test_02:
    (1)用xpath方法定位;
    (2)用WebDriverWait.until和expected_conditions.title_contains方法断言;
test_03:
    (1)通过page_source方法获得网页源码;
    (2)通过正则表达式匹配网站所有的邮箱;
    (3)循环邮箱列表并打印出来;
test_04:
    (1)通过find_element_by_id方法定位;
test_05:
    (1)用find_element_by_link_text方法定位;
test_06:
    (1)用find_element_by_class_name方法定位;
test_07:
    (1)用clear方法清除文本;
test_08:
    (1)页面前进/后退;
test_09:
    (1)通过find_elements_by_nam方法定位;
    (2)单选框radio的选中 ;
test_10:
    (1)多选框checkbox的操作;
    (2)判断多选框是否被选中is_selected();
    (3)查找出选中所有的复选框;
    (4)取消选中的复选框;
test_11:
    (1)查看select中所有的选项select.options;
    (2)查看已选中的选项select.all_selected_options;
test_11:
    (1)查看select中所有的选项select.options;
    (2)查看已选中的选项select.all_selected_options;
test_12:
    (1)提取登录框的文本内容text;
test_13:
    (1)鼠标右键操作actionChains.context_click(element).perform();
    (2)选中某个选项win32api.keybd_event(73,0,0,0);
test_14:
    (1)selenium运行js操作，拖动拖动条;
    (2)弹出一个js提示弹框;
test_15:
    (1)iframe之间的切换；
test_16:
    (1)获取js弹框的文本内容；
    (2)点击弹框的确认按钮;
test_17:
    (1)用find_elements_by_tag_name方法定位；
    (2)遍历所有图片信息;
test_18:
    (1)用get_attribute方法获取页面所有href;
test_19:
    (1)用get_screenshot_as_file方法进行截图;
----------------------------------------------------------------------------------
model_test模块

test_config
    (1)先创建一个config.ini文件;
    (2)创建类TestReadConfigFile读取配置文件内容;
    (3)获取当前项目根目录相对路径：os.path.abspath(os.path.dirname(','));




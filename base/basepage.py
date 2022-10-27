from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
class BasePage:

    # 构造函数 实例化类时 调用
    def __init__(self,driver):
        self.driver = driver

    # 元素定位
    def locator(self,loc):
        # loc = (AppiumBy.ID,"resourceid值")
        # test(*args)：* 的作用其实就是把序列 args 中的每个元素，当作位置参数传进去。比如上面这个代码，
        # 如果 args 等于 (1,2,3) ，那么这个代码就等价于 test(1, 2, 3) 。
        #
        # test(**kwargs)：** 的作用则是把字典 kwargs 变成关键字参数传递。比如上面这个代码，
        # 如果 kwargs 等于 {‘a’:1,’b’:2,’c’:3} ，那这个代码就等价于 test(a=1,b=2,c=3) 。
        return self.driver.find_element(*loc)

    def input(self,loc,value):
        self.locator(loc).send_keys(value)

    def click(self,loc):
        self.locator(loc).click()

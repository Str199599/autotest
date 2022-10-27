from base.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
class LoginPage(BasePage):

    #特有的属性
    el_denglu = (AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="登录，按钮"]/android.widget.FrameLayout/android.widget.ImageView')
    el_user = (AppiumBy.ID,"com.example.myapplication:id/et_1")
    el_pasdenglu = (AppiumBy.ID,"com.example.myapplication:id/et_2")
    el_login = (AppiumBy.ID,"com.example.myapplication:id/btn_login")

    #特有的方法

    def login(self,user,passw):
        # self.click(self.el_denglu)
        self.input(self.el_user,user)
        self.input(self.el_pasdenglu,passw)
        self.click(self.el_login)
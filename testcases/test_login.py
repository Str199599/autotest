import os
from appium import webdriver
import pytest
from pageobjects.login_page import LoginPage
from common.data_util import readYaml
class TestLogin:
    def setup(self):
        rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        path = os.path.join(rootPath, "config\config.yaml")
        data = readYaml(path)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', data["desired_caps"])
    # 执行多个测试用例

    @pytest.mark.parametrize("user,passw",[("123","123"),("123","55"),("123","1234")])
    def test_login(self,user,passw):
        login_page = LoginPage(driver=self.driver)
        login_page.login(user,passw)

if __name__=='__main__':
    pytest.main()
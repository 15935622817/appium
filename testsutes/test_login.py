from testsutes.base_tecase import BaseTestCase
from framework.Logger import Logger
from memorandum.homepage import HomePage
from ddt import data, ddt
from framework.util import Util
import unittest
import time
logger = Logger("testlogin").getlog()
testdata=Util.read_excel("E:/appium/tools/demo.xlsx", "Sheet1")
@ddt
class testlogin(BaseTestCase):
    @data(*testdata)
    def test_Login(self, data):
        self.hp = HomePage(self.driver)
        self.search_user = data["username"]
        self.search_pwd = data["password"]
        print(self.search_user)
        print(self.search_pwd)
        self.hp.login(self.search_user,self.search_pwd)
        try:
            self.assertEqual("智能备忘录",self.driver.find_element(*self.hp.assertmemo).text)
            logger.info("登录成功")
        except Exception as e:
            logger.error("登录失败")
        self.hp.exit_login()
if  __name__ == "__main__":
    unittest.main(verbosity=2)
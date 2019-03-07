from testsutes.base_tecase import BaseTestCase
from framework.Logger import Logger
from memorandum.homepage import HomePage
import unittest
import appium
logger=Logger("register").getlog()
class testRegister(BaseTestCase):
    def test_Register(self):
        self.hp=HomePage(self.driver)
        self.hp.register("LOL","LOL@qq.com","7654321")
        try:
            self.assertEqual("智能备忘录",self.driver.find_element(*self.hp.assertmemo).text)
            logger.info("注册成功")
            print("jjjjjjjjjjjj")
        except Exception as  e:
            logger.error("注册失败")
            print("hhhhhhhhhhhhhhhh")
        self.hp.exit_login()
if __name__=="__main__":
    unittest.main(verbosity=2)


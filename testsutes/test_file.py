from testsutes.base_tecase import BaseTestCase
from framework.Logger import Logger
from memorandum.homepage import HomePage
import unittest
import appium
logger=Logger("test_file").getlog()
class Test_File(BaseTestCase):
    def test_FileCase(self):
        self.hp=HomePage(self.driver)
        self.hp.login("1114805590@qq.com","1234567")
        self.hp.file()
        try:
            self.assertEqual(self.driver.find_element(*self.hp.guidang_assert).text, "归档成功")
            print("kkkkkk")
            logger.info("归档成功")
        except  Exception as e:
            print("hhhhhh")
            logger.error("归档失败")
        self.hp.recoverfile()
        try:
            self.assertEqual(self.driver.find_element(*self.hp.memo_canclefile).text, "备忘录取消回档")
            print("ldccc")
            logger.info("备忘录取消回荡成功")
        except  Exception as  e:
            logger.error("回档失败")
            print("kkkkllllll")
        self.driver.back()
        self.hp.exit_login()

if __name__=="__main__":
    unittest.main(verbosity=2)

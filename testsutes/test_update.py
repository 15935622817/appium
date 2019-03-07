from testsutes.base_tecase import BaseTestCase
from framework.Logger import Logger
from memorandum.homepage import HomePage
import unittest
import time
logger=Logger("testupdata").getlog()
class Testupdata(BaseTestCase):
    def test_updata(self):
        self.hp=HomePage(self.driver)
        self.hp.login("1114805590@qq.com","1234567")
        self.hp.update("nij")
        time.sleep(5)
        try:
            self.assertEqual(self.driver.find_element(*self.hp.updatassert).text,"用户中心")
            logger.info("修改成功")
            print("jjjjjjjjjj")
        except Exception as e:
            logger.error("修改失败")
        self.driver.back()
        self.hp.exit_login()

if __name__=="__main__":
    unittest.main(verbosity=2)
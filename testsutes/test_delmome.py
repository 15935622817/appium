import unittest
from framework.Logger import  Logger
from testsutes.base_tecase import BaseTestCase
from memorandum.homepage import HomePage
import appium
logger=Logger("Test_DelFile").getlog()
class Test_DelFile(BaseTestCase):
    def test_DelCase(self):
        self.hp=HomePage(self.driver)
        self.hp.login("1114805590@qq.com","1234567")
        self.hp.delmemo()

if __name__=="__main__":
    unittest.main(verbosity=2)

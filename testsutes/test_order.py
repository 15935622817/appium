from testsutes.base_tecase import BaseTestCase
from framework.Logger import Logger
from memorandum.homepage import HomePage
import unittest
import appium
logger=Logger("test_order").getlog()
class Test_Order(BaseTestCase):
    def test_OrderCase(self):
        self.hp=HomePage(self.driver)
        self.hp.login("1114805590@qq.com","1234567")
        self.hp.order()
        # self.assertEqual(self.driver.find_element(*self.hp.order_assert),"0301")
        # logger.info('排序成功')
        # print("gggggggggggggg")
        self.driver.back()
        self.hp.exit_login()

if __name__=="__main__":
    unittest.main(verbosity=2)

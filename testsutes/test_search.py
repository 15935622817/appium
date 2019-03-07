from testsutes.base_tecase import BaseTestCase
from framework.Logger import Logger
from memorandum.homepage import HomePage
import unittest
import appium
logger=Logger("testa").getlog()
class TestSearch(BaseTestCase):
    def test_Search(self):
        self.hp=HomePage(self.driver)
        self.hp.login("1114805590@qq.com","1234567")
        self.hp.search("gggggg")
        try:
            self.assertEqual("没有查询到数据",self.driver.find_element(*self.hp.search_assert).text)
            logger.info("搜索成功")
        except  Exception  as  e:
            logger.info("搜索失败")
        self.driver.back()
        self.driver.back()
        self.hp.exit_login()

if __name__=="__main__":
    unittest.main(verbosity=2)
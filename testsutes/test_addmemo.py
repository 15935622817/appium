from testsutes.base_tecase import BaseTestCase
from framework.Logger import Logger
from memorandum.homepage import HomePage
import unittest
import appium
logger=Logger("testa").getlog()
class Test_addmemo(BaseTestCase):
    def test_Addmemo(self):
        self.hp=HomePage(self.driver)
        self.hp.login("1114805590@qq.com","1234567")
        # xx=self.driver.find_elements(*self.hp.addlist)
        # m=len(xx)
        # print(m)
        self.hp.addmemo("mnh")
        # ll= self.driver.find_elements(*self.hp.addlist)
        # n=len(ll)
        # print(n)
        # if n>m:
        #     print("添加成功")
        # else:
        #     print("添加失败")
        try:
            self.assertEqual("mnh",self.driver.find_element(*self.hp.pre_file).text)
            logger.info("添加成功")
        except Exception as e:
            logger.error("添加失败")
        #self.hp.addmemojia("hhhhhhhhhhhh")
if __name__=="__main__":
    unittest.main(verbosity=2)
import unittest
from ddt import data, ddt
from framework.util import Util

from framework.brower_engine import BrowserEngine
import time
import warnings
# testdata=Util.read_excel("D:/demo.xlsx", "Sheet1")
# @ddt
class  BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.be=BrowserEngine()
        warnings.simplefilter("ignore", ResourceWarning)
        self.be.desired_caps["sessionOverride"]=True
        self.be.desired_caps["noReset"]=True
        self.driver = self.be.open_apk()
        time.sleep(10)

    # @data(*testdata)
    # def test_search(self, data):
    #     self.search_user = data["username"]
    #     self.search_pwd = data["password"]
    #     return  self.search_user,self.search_pwd
    #     # print("用户名->：%s" % self.search_user)
    #     # print("密码->：%s" % self.search_pwd)

    def tearDown(self):
        self.be.quit_apk()
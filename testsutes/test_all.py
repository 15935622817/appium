import unittest
from testsutes.test_login import testlogin
from testsutes.test_register import  testRegister
from testsutes.test_update import Testupdata
from testsutes.test_addmemo import Test_addmemo
from testsutes.test_order import Test_Order
from testsutes.test_file import Test_File
from testsutes.test_search import TestSearch
from testsutes.test_delmome import Test_DelFile
import HTMLTestRunner
import os
#获取当前路径testall1文件所在的路径
cur_path=os.path.dirname    (os.path.realpath(__file__))
#将测试报告放在当前路径下的report中
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
#将abc_test ,sort_test加入到suite中
suite=unittest.TestSuite()#实列化suite
suite.addTest(unittest.makeSuite(testRegister))
suite.addTest(unittest.makeSuite(testlogin))
suite.addTest(unittest.makeSuite(Testupdata))
suite.addTest(unittest.makeSuite(Test_addmemo))
suite.addTest(unittest.makeSuite(TestSearch))
suite.addTest(unittest.makeSuite(Test_Order))
suite.addTest(unittest.makeSuite(Test_File))
suite.addTest(unittest.makeSuite(Test_DelFile))
if __name__=="__main__":
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试",description="用例执行情况")
    runner.run(suite)
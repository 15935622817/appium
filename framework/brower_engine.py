import os.path
from  configparser import ConfigParser
import  os
from appium import  webdriver
from  framework.Logger import Logger

logger=Logger(logger="BrowserEngine").getlog()
class  BrowserEngine(object):
    def __init__(self):
        self.apk_path = os.path.dirname(os.path.abspath("."))
        self.desired_caps = {}
        self.desired_caps["app"] = self.apk_path + "/app/znbwl.apk"
    def open_apk(self):
        config=ConfigParser()
        #读取config.ini的路径
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"
        config.read(file_path,encoding="utf-8")
        self.desired_caps["platformName"]=config.get("apkType","platformName")
        self.desired_caps["platformVersion"]= config.get("apkType", "platformVersion")
        self.desired_caps["deviceName"]=config.get("apkType", "deviceName")
        self.desired_caps["appPackage"]=config.get("name","appPackage")
        self.desired_caps["appActivity"] = config.get("name","appActivity")

        logger.info("选择apk类型%s"%self.desired_caps["platformName"])
        logger.info("版本是%s"%self.desired_caps["platformVersion"])
        logger.info("设备名字是%s" %self.desired_caps["deviceName"])
        url=config.get("testServer","URL")
        logger.info("测试链接是%s"%url)

        #实例化driver

        self.driver=webdriver.Remote(url,self.desired_caps)
        logger.info("打开安卓系统")
        # self.driver.get(url)
        #logger.info(   "打开链接%s"%url)
        self.driver.implicitly_wait(10)
        logger.info("等 10s")
        return  self.driver
    def quit_apk(self):
        self.driver.quit()
        logger.info("离开app")

# BrowserEngine().open_apk()
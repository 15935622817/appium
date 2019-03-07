import os.path
import  os
from appium import  webdriver
from  framework.Logger import Logger
import yaml

logger=Logger(logger="BrowserEngine").getlog()
class  BrowserEngine(object):
    def __init__(self):
        self.apk_path = os.path.dirname(os.path.abspath("."))
        self.desired_caps = {}
        self.desired_caps["app"] = self.apk_path + "/app/znbwl.apk"
    def open_apk(self):

        #读取config.ini的路径
        file_path=os.path.dirname(os.path.abspath("."))+"/yaml/gg.yaml"
        with  open(file_path,"r",encoding="utf-8") as file:
            data=yaml.load(file)
        self.desired_caps["platformName"]=data["platformName"]
        self.desired_caps["platformVersion"]=data['platformVersion']
        self.desired_caps["deviceName"]=data['deviceName']
        self.desired_caps["appPackage"]=data['appPackage']
        self.desired_caps["appActivity"] = data['appActivity']
        self.desired_caps['ip']=data['ip']
        self.desired_caps['port']=data['port']
        self.desired_caps['sessionOverride']=data['sessionOverride']
        self.desired_caps['noReset']=data['noReset']
        logger.info("选择apk类型%s"%self.desired_caps["platformName"])
        logger.info("版本是%s"%self.desired_caps["platformVersion"])
        logger.info("设备名字是%s" %self.desired_caps["deviceName"])
        #实例化driver
        self.driver=webdriver.Remote('http://'+ str(data['ip']) +':'+ str(data['port']) + 	'/wd/hub',self.desired_caps)
        logger.info('http://'+ str(data['ip']) +':'+ str(data['port']) + 	'/wd/hub')
        logger.info("打开安卓系统")
        self.driver.implicitly_wait(10)
        logger.info("等 10s")
        return  self.driver
    def quit_apk(self):
        self.driver.quit()
        logger.info("离开app")

BrowserEngine().open_apk()
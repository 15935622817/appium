import os
from appium import webdriver

apk_path=os.path.dirname(os.path.abspath('.'))
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='5.1.1'
desired_caps['deviceName']='127.0.0.1:62001'  #62001
desired_caps['sessionOverride']=True

desired_caps['app']=apk_path+'/app/znbwl.apk'
# print(apk_path)
desired_caps['noReset']=True
desired_caps['appPackage']='com.example.znbwl'
desired_caps['appActivity']='com.example.znbwl.LoginActivity'

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
import  os
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
apk_path=os.path.dirname(os.path.abspath("."))
#字典
desired_caps={}
desired_caps["platformName"]="android"#设备系统
desired_caps["platformVersion"]="5.1.1" #设备系统版本
desired_caps["deviceName"]="127.0.0.1:62001" #设备名称
#等于true时每次运行覆盖
desired_caps["sessionOverride"]=True
#测试apk包的路径
desired_caps["app"]=apk_path+"/app/todolist.apk"
#不需要每次都安装apk
desired_caps["noReset"]=True
#应用程序包名 进入abbt文件夹下可以输入aapt d badging todolist.apk命令可获取
desired_caps["appPackage"]="com.example.todolist"
#启动程序包名
desired_caps["appActivity"]="com.example.todolist.LoginActivity"
#打开app
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
#登录
driver.find_element_by_id("nameET").send_keys("1")
driver.find_element_by_id("passwordET").send_keys("1")
driver.find_element_by_id("loginBtn").click()
#添加
driver.find_element_by_id("action_new").click()
driver.find_element_by_id("toDoItemDetailET").send_keys("sunshne")
driver.find_element_by_id("saveBtn").click()

#长安
action=TouchAction(driver)
el=driver.find_element_by_id("com.example.todolist:id/toDoItemDetailTv")
action.long_press(el).wait(10000).perform()
print("...........")
time.sleep(8)
#删除
driver.find_element_by_name("删除").click()
driver.find_element_by_id("android:id/button1").click()
print("ckdckskmsckmk")
#退出
driver.find_element_by_class_name("android.widget.ImageButton").click()
driver.find_element_by_id("android:id/title").click()
driver.find_element_by_name("确定").click()


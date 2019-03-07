# from selenium.webdriver.support.wait import  WebDriverWait
# from selenium.webdriver.support import  expected_conditions as  EC
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
from  framework.Logger import Logger
import time
import os.path

logger=Logger(logger="base").getlog()

class BasePage(object):
    #初始化driver
    def __init__(self,driver):
        self.driver=driver    #返回
    def back(self):
        self.driver.back()
        logger.info("返回当前页面")
    #前进
    def forward(self):
        self.driver.forward()
        logger.info("前进")
    #打开网页链接
    def open_url(self, url):
        self.driver.get(url)
        logger.info("open%s"%url)
    #离开浏览器
    def quit_apk(self):
        self.driver.quit()
        logger.info("quit apk")
    #获取当前窗口
    def switch_window(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    #获取当前打开的窗口
    def handlers(self,i):
        self.driver.switch_to.window(self.driver.window_handles[i])
    #进入iframe
    def goiframe(self,n):
        self.driver.switch_to.frame(n)
    #窗口最大
    def max_window(self):
        self.driver.maximize_window()
    #f5刷新
    def  F5(self):
        self.driver.refresh()
    #等待时间隐士等待
    def  wait(self,waittime):
        self.driver.implicitly_wait(waittime)
    #获得控件元素的文本信息
    def get_text(self,*loc):
        return  self.find_element(loc).text
    #获取属性值，type为css，id，。。。。
    def get_attribute(self,*loc,type):
        return self.find_element(loc).get_attribute(type)
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭离开浏览器")
        except Exception as e:
            logger.error("失败离开浏览器")

    def find_element(self,*loc):
        try:
            # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            self.driver.find_element(*loc)
            logger.info("找到页面元素")
            return self.driver.find_element(*loc)
        except Exception as  e:
            logger.error("页面未找到元素")
            #截屏
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/screenshots/"
        rq=time.strftime("%Y%m%d%H%%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("有截屏并且保存的路径是/screenshots/")
        except  Exception as  e:
            self.get_windows_img()
            logger.error("截屏失败")
    def  sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容%s"%text)
        except  Exception  as e:
            logger.info("失败输入内容%s"%e)
            self.get_windows_img()
    def clear(self,*loc):
        el=self.find_element(*loc)

        try:
            el.clear()
            logger.info("键入前清除文本框的内容")
        except Exception  as e:
            logger.error("%s清楚文本框内容失败"%e)
            self.get_windows_img()
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("被点击%s"%el)
        except Exception  as e:
            logger.error("没被点击%s"%el)
    #回车
    def enter(self):
        try:
            # self.driver.KeyEvent(66)
            self.driver.press_keycode(66)
            logger.info("回车成功")
        except  Exception  as  e:
            logger.error("回车失败")
            self.get_windows_img()
    #长安
    def long_pre(self,*loc):
        try:
            action = TouchAction(self.driver)
            ee = self.find_element(*loc)
            action.long_press(ee).wait(10000).perform()
            logger.info("长安成功")
        except  Exception  as  e:
            logger.error("长按失败")
            self.get_windows_img()
    #滑动
    def swipe(self,startx, starty, endx, endy,duration):
        try:
            self.driver.swipe(startx, starty, endx, endy,duration)
            logger.info("滑动成功")
        except  Exception as  e:
            logger.error("滑动失败")
            self.get_windows_img()
    #按压滑动
    def  pre_swipe(self,*loc,x,y,x1,y1, time):
        try:
            actions=TouchAction(self.driver)
            element=self.find_element(*loc)
            actions.press(element,x,y).wait(time).move_to(element,x1,y1).release().perform()
            logger.info("滑动成功")
        except  Exception  as  e:
            logger.error("滑动失败")
            self.get_windows_img()
    #获取元素文本内容
    def getText(self,*loc):
         return  self.find_element(*loc).text
    #查找列表
    def find_elements(self,*loc):
        try:
            # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            self.driver.find_elements(*loc)
            logger.info("找到list")
            return self.driver.find_elements(*loc)
        except Exception as  e:
            logger.error("页面未找到list")

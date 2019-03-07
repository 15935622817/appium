from  memorandum.base import BasePage
from framework.Logger import Logger
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction
import appium
import  time

logger = Logger("homepage").getlog()
class HomePage(BasePage):
    #  注册
    menu = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
    register_b = (By.ID, "com.pdswp.su.smartcalendar:id/email")
    registerUser = (By.ID, "com.pdswp.su.smartcalendar:id/register")
    username = (By.ID, "com.pdswp.su.smartcalendar:id/username")
    registerMail = (By.ID, "com.pdswp.su.smartcalendar:id/email")
    password = (By.ID, "com.pdswp.su.smartcalendar:id/password")
    register_btu = (By.ID, "com.pdswp.su.smartcalendar:id/reguser")
    exit_btu=(By.ID,"com.pdswp.su.smartcalendar:id/exit")
    #登录
    # menu_login= (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")
    lb = (By.ID, "com.pdswp.su.smartcalendar:id/username")
    email = (By.ID,'com.pdswp.su.smartcalendar:id/email')
    passwordb = (By.ID,"com.pdswp.su.smartcalendar:id/password")
    login_btn = (By.ID,"com.pdswp.su.smartcalendar:id/login")
    assertmemo=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")

    #修改用户名
    updat_jianjian=(By.ID,"com.pdswp.su.smartcalendar:id/imageView4")
    update_username=(By.CLASS_NAME,"android.widget.EditText")
    update_duigou=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    updatassert=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")

    #添加备忘录
    memo_btu=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")
    memo_infomation=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")
    memo_textinput=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")
    memo_duigou=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")

    memo_jia=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")


    #搜索
    search_btu=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")
    search_input=(By.ID,"android:id/search_src_text")
    # return_jianjian=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")
    quxiao=(By.NAME,"取消")
    #排序

    setting=(By.NAME,"应用设置")
    order_data=(By.ID,"com.pdswp.su.smartcalendar:id/set_timesortnew")
    order_assert=(By.CSS_SELECTOR,"#com.pdswp.su.smartcalendar:id/note_time:last-of-type")

    #归档
    pre_file=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    save_file=(By.ID,"com.pdswp.su.smartcalendar:id/menu_archive")
    msaveFile=(By.NAME,"归档")
    guidang_assert=(By.NAME,"归档成功")
    detail_file=(By.ID,"com.pdswp.su.smartcalendar:id/note_time")
    return_file=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")
    recover=(By.NAME,"恢复")
    memo_canclefile=(By.NAME,"备忘录取消回档")

    #删除备忘录
    del_btu=(By.ID,"com.pdswp.su.smartcalendar:id/menu_delete")
    recycled=(By.NAME,"回收站")
    claer_recycled=(By.ID,"com.pdswp.su.smartcalendar:id/button")
    quare=(By.ID,"com.pdswp.su.smartcalendar:id/material_background")
    btn_area=(By.ID,"com.pdswp.su.smartcalendar:id/buttonLayout")
    confim_del = (By.NAME,"确定")
    # ass=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")

    #
    addlist=(By.ID,"com.pdswp.su.smartcalendar:id/notelistview")
    search_assert=(By.NAME,"没有查询到数据")
    def register(self, name, email, pwd):
        self.click(*self.menu)
        self.click(*self.register_b)
        self.click(*self.registerUser)
        self.sendkeys(name,*self.username)
        self.sendkeys(email,*self.registerMail)
        self.sendkeys(pwd,*self.password)
        self.click(*self.register_btu)
        time.sleep(10)
    def exit_login(self):
        time.sleep(5)
        self.click(*self.menu)
        time.sleep(5)
        self.click(*self.register_b)
        time.sleep(5)
        self.click(*self.exit_btu)
        time.sleep(5)
    #登录
    def login(self,email,passw):
        self.click(*self.menu)
        time.sleep(5)
        self.click(*self.lb)
        time.sleep(5)
        self.sendkeys(email,*self.email)
        self.sendkeys(passw,*self.passwordb)
        self.click(*self.login_btn)


    #修改用户名
    def update(self,uname):
        time.sleep(5)
        self.click(*self.menu)
        time.sleep(5)
        self.click(*self.register_b)
        time.sleep(5)
        self.click(*self.updat_jianjian)
        time.sleep(5)
        self.sendkeys(uname,*self.update_username)
        time.sleep(5)
        self.click(*self.update_duigou)



    def addmemo(self,detailmome):
        time.sleep(5)
        self.click(*self.menu)
        time.sleep(5)
        self.click(*self.memo_btu)
        time.sleep(5)
        # self.sendkeys(information,*self.memo_infomation)
        self.sendkeys(detailmome,*self.memo_textinput)
        self.click(*self.update_duigou)
        self.exit_login()
    def addmemojia(self,content):
        time.sleep(5)
        self.click(*self.memo_jia)
        self.sendkeys(content,*self.memo_textinput)
        self.click(*self.update_duigou)
        self.exit_login()
    def search(self,content):
        self.click(*self.search_btu)
        self.sendkeys(content, *self.search_input)
        self.enter()

    def order(self):
        self.click(*self.menu)
        self.click(*self.setting)
        self.click(*self.order_data)
    #归档
    def file(self):
        time.sleep(5)
        self.long_pre(*self.pre_file)
        time.sleep(3)
        self.click(*self.save_file)
        # self.assertEqual(self.find_element(*self.guidang_assert).text,"归档成功")
        # logger.info("归档成功")
    def  recoverfile(self):
        time.sleep(3)
        self.click(*self.menu)
        time.sleep(3)
        self.click(*self.msaveFile)
        time.sleep(3)
        self.click(*self.detail_file)
        time.sleep(3)
        self.click(*self.return_file)
        time.sleep(3)
        self.swipe(700, 161, 350, 176, 1000)
        time.sleep(5)
        self.click(*self.recover)

    def delmemo(self):
        time.sleep(5)
        self.long_pre(*self.pre_file)
        time.sleep(3)
        self.click(*self.del_btu)
        time.sleep(4)
        self.click(*self.menu)
        time.sleep(4)
        self.click(*self.recycled)
        time.sleep(4)
        self.click(*self.detail_file)
        time.sleep(4)
        self.click(*self.return_file)
        time.sleep(4)
        self.click(*self.claer_recycled)
        time.sleep(4)
        self.find_element(*self.quare)
        self.click(*self.confim_del)
        time.sleep(5)
        self.back()
        time.sleep(5)
        self.exit_login()



















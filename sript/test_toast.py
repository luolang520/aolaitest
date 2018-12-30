import os,sys
sys.path.append(os.getcwd())
import pytest,page


from page.navigation_page import NavigtiongPage
from base.init_driver import get_driver
import time
from base.read_yaml_data import read_yaml_data


def get_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    print(data)
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")
        passwd = data2.get("password")
        data_list.append((name, passwd))
    return data_list

class TestLogin:
    #初始化导航类
    def setup_class(self):
        #1.初始化driver对象
        self.driver = get_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        #2.初始化导航对象
        self.navigation_page = NavigtiongPage(self.driver)
    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()

    # def test_login2(self):
    #     # 点击我的
    #     self.navigation_page.get_setting_page_obj().clice_my_button()
    #     # 点击已有账号
    #     self.navigation_page.get_sign_in_page_obj().click_exit_accout()
    #     # 输入用户名密码 点击登陆
    #     self.navigation_page.get_login_page_obj().login_in("十里蓝山","1111")
    #     # 提示此用户不存在获取吐司的内容
    #     toast_message=self.navigation_page.setting_page_obj().find_element(page.toast_test)
    #     #打印toast的消息
    #     print(toast_message.text)
    #
    def test_login(self):
        # 1.点击我的
        self.navigation_page.get_home_page_obj().click_my_button()
        # 2.点击已有账号
        self.navigation_page.get_sign_in_page_obj().click_exist_accout()
        # 3.输入用户名密码 点击登录
        self.navigation_page.get_login_page_obj().login_in("十里蓝山", "111")
        #.4.获取toast的内容
        toast_message = self.navigation_page.get_setting_page_obj().find_element(page.toast_test)
        #5.打印toast的消息
        print(toast_message.text)

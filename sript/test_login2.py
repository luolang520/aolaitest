import os,sys

import pytest

sys.path.append(os.getcwd())
from page.navigation_page import NavigtiongPage
from base.init_driver import get_driver
import time,allure
from base.read_yaml_data import read_yaml_data


def get_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    print(data)
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")
        passwd = data2.get("password")
        tag =data2.get("tag")
        except_msg = data2.get("except_msg")
        get_toast_msg = data2.get("get_toast_msg")
        data_list.append((name, passwd,tag,get_toast_msg,except_msg))
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

    # #测试错误的逻辑
    # @pytest.mark.parametrize("username,password,tag,get_toast_msg,except_msg", get_data())
    # def test_login2(self, username,password,tag,get_toast_msg,except_msg):
    #     self.navigation_page.get_person_centenr_page_obj().get_screen()
    #     # 点击我的
    #     self.navigation_page.get_home_page_obj().click_my_button()
    #     # # 点击已有账号
    #     self.navigation_page.get_sign_in_page_obj().click_exist_accout()
    #     # # 输入用户名密码 点击登陆
    #     self.navigation_page.get_login_page_obj().login_in(username, password)
    #     # # 获取，真正的弹出吐司的消息
    #     if tag == 1:
    #         #说明登陆成功校验下是否真的成功，个人中心有一个全部订单
    #         try:
    #            login_state= self.navigation_page.get_person_centenr_page_obj().is_login_sucess()
    #            self.navigation_page.get_person_centenr_page_obj().click_person_center_setting()
    #            self.navigation_page.get_setting_page_obj().logout_account()
    #            assert login_state,self.navigation_page.get_person_centenr_page_obj().get_screen()
    #         except:
    #             # 6.截图 在哪一个页面出现的问题
    #             self.navigation_page.get_person_centenr_page_obj().get_screen()
    #             self.navigation_page.get_login_page_obj().close_login_page()
    #         #toast_msg = self.navigation_page.get_setting_page_obj().get_toast_message(get_toast_msg)
    #
    #     else:
    #         # 关闭当前登陆页面
    #         try:
    #             toast_memssage = self.navigation_page.get_person_centenr_page_obj().get_toast_message(get_toast_msg)
    #             assert toast_memssage == except_msg,self.navigation_page.get_person_centenr_page_obj().get_screen()
    #         finally:
    #             self.navigation_page.get_login_page_obj().close_login_page()
    #
    # 测试登录正确业务
    @pytest.mark.parametrize("username,password,tag,get_toast_msg,except_msg", get_data())
    def test_login(self, username, password, tag, get_toast_msg, except_msg):
        # 1.点击我的

        self.navigation_page.get_home_page_obj().click_my_button()
        # 2.点击已有账号
        self.navigation_page.get_sign_in_page_obj().click_exist_accout()
        # 3.输入用户名密码 点击登录
        self.navigation_page.get_login_page_obj().login_in(username, password)
        if tag == 1:
            try:
                login_state = self.navigation_page.get_person_centenr_page_obj().is_login_sucess()
                # 4.点击个人中心设置按钮
                self.navigation_page.get_person_centenr_page_obj().click_person_center_setting()
                # 5.点击退出
                self.navigation_page.get_setting_page_obj().logout_account()
                assert login_state,self.navigation_page.get_person_centenr_page_obj().get_screen()
            except:
                #6.截图 在哪一个页面出现的问题
                self.navigation_page.get_person_centenr_page_obj().get_screen()
                self.navigation_page.get_login_page_obj().close_login_page()
        else:
            try:
                toast_message = self.navigation_page.get_person_centenr_page_obj().get_toast_message(get_toast_msg)
                assert toast_message == except_msg,self.navigation_page.get_person_centenr_page_obj().get_screen()
            finally:
                # 5.关闭当前登录页面
                self.navigation_page.get_login_page_obj().close_login_page()

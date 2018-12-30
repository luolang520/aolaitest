#负责登陆页面的逻辑
import allure
import page

from base.base_actiton import BaseAciton

class LoginPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)

    @allure.step('登陆逻辑')
    def login_in(self,name,pwd):
        #输入账号账号的数据不能写死 应该是从脚本里面动态的传入
        allure.attach('登录', '请输入账号')
        self.send_element_content(page.login_usernam_id,name)
        #输入密码
        allure.attach('登录', '请输入密码')
        self.send_element_content(page.login_password_id, pwd)
        #链接登陆
        allure.attach('登录', '点击登录按钮')
        self.click_element(page.login_login_in_btn)
        #关闭登陆页面

    def close_login_page(self):
        self.click_element(page.login_login_out_btn)
        pass

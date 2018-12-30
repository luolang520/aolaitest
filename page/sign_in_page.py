
from base.base_actiton import BaseAciton
import page
import allure
#负责注册页面的
class SignInPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
    @allure.step('点击已有账号')
    def click_exist_accout(self):
        self.click_element(page.sign_in_exit_account_id)

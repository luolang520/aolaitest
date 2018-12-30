from base.base_actiton import BaseAciton
import page
import allure
#负责首页分类购物车 我的业务
class HomePage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
    @allure.step('点击我的')
    def click_my_button(self):
        self.click_element(page.home_my_button)
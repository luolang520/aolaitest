
from base.base_actiton import BaseAciton
import page
#负责页面中心逻辑
class PersonconterPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
        #点击个人中心的设置按钮
    def  click_person_center_setting(self):
        self.click_element(page.person_center_setting_btn)
    #判断一下是否登陆成功

    def is_login_sucess(self):
        try:
            self.find_element(page.person_center_all_order)
            return True
        except:
            return False

